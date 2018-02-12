import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def index():
    if "ranNum" not in session:
        session["ranNum"]=random.randrange(0,101)
    print "This session's random number is:", session["ranNum"]
    return render_template('index.html')
    

@app.route("/result", methods=["POST"])
def result():
    pick = request.form["pick"]
    # lastPick = "Your pick is:", request.form["pick"]
    

    if int(request.form["pick"]) > session["ranNum"]:
        result = "Your pick is too high! Sorry, bruh."

    elif int(request.form["pick"]) < session["ranNum"]:
        result = "Your pick is too low! C'mon, man!"

    elif int(request.form["pick"]) == session["ranNum"]:
        result = "You win!!!!!!"

    else:
        result = "Please enter a number from 1-100, you chowderhead."

    return render_template ("index.html", pick=pick, result = result)


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


app.run(debug=True)