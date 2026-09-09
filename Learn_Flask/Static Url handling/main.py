from flask import Flask,render_template

# app = Flask(__name__, static_url_path= "/public") #this is how you can change static folder location
# app = Flask(__name__, static_folder="assests", static_url_path="/public") #this is how you can change static folder location
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


app.run(debug=True)