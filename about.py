from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def about():
    sports=["crossfit","yoga","boxsing","judo","MMA"]
    return render_template("about.html",list_of_sport=sports)