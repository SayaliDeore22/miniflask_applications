"""
Create a flask app to render a HTML page such that it shows how many times the page has been viewed.
"""

from flask import Flask, render_template

app = Flask(__name__)

counter = 0


@app.route("/")
def get_count():
    global counter
    counter += 1
    return render_template("dynamic_view.html", content=counter)


if __name__ == "__main__":
    app.route(host="localhost",port=5000)
