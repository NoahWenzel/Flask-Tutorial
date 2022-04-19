from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Pages on the app
@app.route("/")
def home(name=''):
    return render_template("tutorial_4/index_4.html")

@app.route("/login/", methods=["POST", "GET"])
def login():
    return render_template()

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    