from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "anystringhere"
app.permanent_session_lifetime = timedelta(minutes=3)

@app.route("/")
def home(name=''):
    return render_template("tutorial_6/base_6.html")


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash(f"{user} is now logged in!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(session["user"], " is already logged in!")
            return redirect(url_for("user"))
        return render_template("tutorial_6/login.html")


@app.route("/user/")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("tutorial_6/user_6.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"{user} has been Logged out!", "info")

    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)