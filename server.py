import os
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

# Read port selected by the cloud for our application
port = int(os.getenv('PORT', 8000))

form = { "lol": 1 }

@app.route("/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    print(render_template('chart.html', values=values, labels=labels))
    return render_template('chart.html', values=values, labels=labels)

@app.route("/actoboard", methods=["GET", "POST"])
def actoboard():
    global form
    if request.method == "POST":
        form = request.form
    elif request.method == "GET":
        return str(form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
