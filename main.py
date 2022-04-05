# backend for Wacko's Movie Theater
# Author: Sydney Wells

from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "bjhdsa8U21"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/wics_scavenger_hunt", methods=['GET', 'POST'])
def sh():
    if request.method == "POST":
        if request.form["usern"] == "admin":
            if request.form["userp"] == "helloWorld":
                user = request.form["usern"]
                session["user"] = user
                return redirect(url_for("sh_success"))
            else:
                flash("incorrect username or password", "info")
                return render_template("sh_2022.html")
        else:
            flash("incorrect username or password", "info")
            return render_template("sh_2022.html")
    else:
        return render_template("sh_2022.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    #form = LoginForm()
    if request.method == "POST":
        if request.form["un"] == "admin":
            if request.form["up"] == "admin":
                user = request.form["un"]
                session["user"] = user
                return redirect(url_for("admin"))
            else:
                flash("incorrect username or password", "info")
                return render_template("auth/log_in.html")
        else:
            flash("incorrect username or password", "info")
            return render_template("auth/log_in.html")
    else:
        return render_template("auth/log_in.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/daphne")
def daphne():
    return render_template("daphne.html")

@app.route("/persephone")
def perse():
    return render_template("perse.html")

@app.route("/success", methods = ["GET", "POST"])
def sh_success():
    return render_template("sh_p2.html") 


if __name__ == "__main__":
    app.run(debug=True)
