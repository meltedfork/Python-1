from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "supersecret"

import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[aA-zZ\s]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=["POST"])
def result():
    firstname = request.form["first_name"]
    lastname = request.form["last_name"]
    email=request.form["email"]
    password=request.form["password"]
    confirm=request.form["confirm"]


    if len(firstname) < 1:
       flash("First name field cannot be empty!")
       return redirect("/")
    
    elif len(email) < 1:
        flash("Email field cannot be empty!")
        return redirect("/")

    elif len(lastname) < 1:
        flash("Last name field cannot be empty!")
        return redirect("/")
    
    elif len(password) < 8:
        flash("Password must have more than 8 characters!")
        return redirect("/")
    
    elif confirm != password:
        flash("Passwords do not match!")
        return redirect("/")

    elif not EMAIL_REGEX.match(request.form["email"]):
        flash ("Email must be a valid email.")
        return redirect("/")
    
    elif not NAME_REGEX.match(firstname):
        flash("First name must be a valid and contain no numbers.")
        return redirect("/")

    elif not NAME_REGEX.match(lastname):
        flash("Last name must be a valid and contain no numbers.")
        return redirect("/")

    else:
        flash("Thanks for submitting!")
    
    return redirect("/")

app.run(debug=True)