from flask import Flask, render_template

app = Flask("Website")

@app.route("/home")
def home():
    return render_template("Tutorial.html")

@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)