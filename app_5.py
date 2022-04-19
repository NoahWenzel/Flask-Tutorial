from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "anystringhere"
app.permanent_session_lifetime = timedelta(minutes=3)

@app.route("/")
def home(name=''):
    return render_template("tutorial_4/index_4.html")


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("tutorial_4/login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
