from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "supersecret"


@app.route('/')

def index():
    count=session["count"]
    if "count" in session:
        session["count"] += 1
    else:    
        session["count"] = 0
    print "This works."
    return render_template('index.html', count=count)


@app.route('/two', methods=["POST"])

def two():
    session["count"] += 1
    return redirect("/")

@app.route("/reset", methods=["POST"])

def reset():
    session["count"]=1
    return redirect("/")
    


app.run(debug=True)