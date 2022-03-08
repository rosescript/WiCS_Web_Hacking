# backend for Wacko's Movie Theater
# Author: Sydney Wells

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

#TODO: hook this thing up to a database
#TODO: set up login route
#TODO: contact form for injection attack?
 

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    #form = LoginForm()
    return render_template("auth/log_in.html")



if __name__ == "__main__":
    app.run(debug=True)