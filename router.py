from flask import Flask
from flask.templating import render_template
import weather_api as wt

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", weathers=wt.callWeathApi())


if __name__ == "__main__":
    app.run(debug=True)
