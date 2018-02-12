import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template('index.html', gold = session['gold'], activities = session['activities'])
    

@app.route("/process_money", methods=["GET","POST"])
def result():
    if request.form["action"] == "farm":
        pay = random.randrange(10,21)
        session["gold"] += pay
        session["activities"].append(str(pay)+ " Gold earned.")

    elif request.form["action"] == "cave":
        pay = random.randrange(5,11)
        session["gold"] += pay
        session["activities"].append(str(pay) + " Gold earned.")

    elif request.form["action"] == "house":
        pay = random.randrange(2,6)
        session["gold"] += pay
        session["activities"].append(str(pay)+ " Gold earned.")

    elif request.form["action"] == "casino":
        pay = random.randrange(-50,51)
        if pay >= 0:
            session["gold"] += pay
            session["activities"].append(str(pay) + " Gold earned.")
        elif pay < 0:
            session["gold"] += pay
            session["activities"].append(str(pay) + " Gold lost.")

    elif request.form["action"] == "restart":
        session["gold"] = 0
        session["activities"] = []
        
    return redirect("/")


app.run(debug=True)