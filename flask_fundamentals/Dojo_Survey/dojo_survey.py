from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    print "Got Post info"
    name = request.form["name"]
    if len(request.form["name"]) < 1:
       flash("Name field cannot be empty!")
       errors= True
    else:
        flash("Sweet name, bruh.")
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]
    if len(request.form["comments"]) < 1:
        flash("You gotta have some thoughts!")
        errors = True
    elif len(comments) > 120:
        flash("Too long, didn't read.")
        errors = True
    # location = request.form[""]
    # print name    
    return render_template('/')

app.run(debug=True)