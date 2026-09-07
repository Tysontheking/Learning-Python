from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"] )
def hello_world():
    with open("data.txt",'w') as f:
        f.write(f"Name is {request.form}")
    print(request.method)
    return render_template("contact.html")

app.run(debug=True)