from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv("data_small/TG_STAID" + str(station).zfill(6) + ".txt")
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5001)

# using jupyter in later projects
# another commit

