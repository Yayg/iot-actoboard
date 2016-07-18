import os
import time
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

# Read port selected by the cloud for our application
port = int(os.getenv('PORT', 8000))

data = { "lumiere": 0, "humidity": 0, "temperature": 0, "distance": 0 }
time = time.time()

@app.route("/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    print(render_template('chart.html', values=values, labels=labels))
    return render_template('chart.html', values=values, labels=labels)

@app.route("/actoboard", methods=["GET", "POST"])
def actoboard():
    global data
    if request.method == "POST":
        data["lumiere"] = request.data.get("slot_lumiere")
        data["humidity"] = request.data.get("slot_humidity")
        data["temperature"] = request.data.get("slot_temperature")
        data["distance"] = request.data.get("slot_distance")
    elif request.method == "GET":
        return str(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
