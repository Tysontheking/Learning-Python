from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John":45,
        "Sux":75,
        "Kix":85,
        "Sath":45,
        "Alex":15,
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)