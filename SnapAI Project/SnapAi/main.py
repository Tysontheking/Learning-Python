from flask import Flask, render_template, request
import uuid
import os

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "user_uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        print("Files received:", request.files.keys())

        rec_id = request.form.get("uuid")
        doc = request.form.get("text", "")

        # Create folder for this project
        upload_dir = os.path.join(
            app.config["UPLOAD_FOLDER"],
            rec_id
        )

        os.makedirs(upload_dir, exist_ok=True)

        # --------------------------------
        # Save description
        # --------------------------------

        description_path = os.path.join(
            upload_dir,
            "Description.txt"
        )

        with open(
            description_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(doc)

        # --------------------------------
        # Create FFmpeg concat file
        # --------------------------------

        input_txt_path = os.path.join(
            upload_dir,
            "input.txt"
        )

        # "w" is important.
        # It prevents old filenames from remaining in the file.
        with open(
            input_txt_path,
            "w",
            encoding="utf-8"
        ) as f:

            for key, uploaded_file in request.files.items():

                # Ignore empty file fields
                if not uploaded_file or not uploaded_file.filename:
                    continue

                original_filename = uploaded_file.filename

                # Sanitize filename
                filename = secure_filename(original_filename)

                # Make sure extension is allowed
                extension = filename.rsplit(".", 1)[-1].lower()

                if extension not in ALLOWED_EXTENSIONS:
                    print(
                        f"Skipping unsupported file: {original_filename}"
                    )
                    continue

                # --------------------------------
                # Save uploaded file
                # --------------------------------

                file_path = os.path.join(
                    upload_dir,
                    filename
                )

                uploaded_file.save(file_path)

                print(f"Saved: {file_path}")

                # --------------------------------
                # Add file to FFmpeg input.txt
                # --------------------------------

                # Quotes are IMPORTANT because filenames
                # may contain spaces.
                f.write(f"file '{filename}'\n")
                f.write("duration 1\n")

        print(f"Created: {input_txt_path}")

        # Show generated input.txt in terminal
        print("\n----- input.txt -----")

        with open(
            input_txt_path,
            "r",
            encoding="utf-8"
        ) as f:
            print(f.read())

        print("---------------------\n")

    myid = uuid.uuid1()

    return render_template(
        "create.html",
        myid=myid
    )


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)