from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Pages on the app
@app.route("/")
def home(name=''):
    return render_template("tutorial_4/index_4.html")

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("tutorial_4/login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
    