from flask import Flask
from datetime import datetime
from pyts import timezone

app = Flask(__name__)

@app.route("/")
def time():
    now = datetime.new(timezone('America/Salt_Lake_City'))
    return "The current date and time in Salt Lake City is {}".format(now)