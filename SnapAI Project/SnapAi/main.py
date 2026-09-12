from flask import Flask, render_template,request
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods = ["GET","POST"])
def create():
    if request.method == "POST":
        print(request.files.keys())
        for key, value in request.files.items():
            print(key,value)
    myid = uuid.uuid1()
    return render_template("create.html", myid = myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)