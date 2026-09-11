from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Maths": 90,
        "Science": 85,
        "English": 88,
        "History": 92
    }
    values = [12, 34, 56, 78,marks]
    return jsonify(values)


app.run(debug=True) 