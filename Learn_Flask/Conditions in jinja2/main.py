from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Maths": 90,
        "Science": 85,
        "English": 88,
        "Hindi": 92,
        "History": 0
        
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)