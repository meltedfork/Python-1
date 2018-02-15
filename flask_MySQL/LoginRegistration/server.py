from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key= "12345"
import re, md5, os, binascii
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[aA-zZ\s]+$')

mysql = MySQLConnector(app,'loginregister')


@app.route('/')
def index():
    if "user_id" in session:
        # print session["user_id"]
        return redirect("/welcome")
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/success')
def success():
    # query = "Select name from users where id = :id"
    # parameters= {"id":session['user_id']}
    return render_template("success.html")

@app.route('/register', methods = ["POST"])
def register():
    
    errors = []
    firstname = request.form["first_name"]
    lastname = request.form["last_name"]
    email=request.form["email"]
    password=request.form["password"]
    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()
    confirm=request.form["confirm"]


    if len(firstname) < 2:
       errors.append("First name field cannot be empty!")
    
    if len(email) < 1:
        errors.append("Email field cannot be empty!")

    if len(lastname) < 2:
        errors.append("Last name field cannot be empty!")
    
    if len(password) < 8:
        errors.append("Password must have more than 8 characters!")
    
    if confirm != password:
        errors.append("Passwords do not match!")

    if not EMAIL_REGEX.match(request.form["email"]):
        errors.append("Email must be a valid email.")
    
    if not NAME_REGEX.match(firstname):
        errors.append("First name must be a valid and contain no numbers.")

    if not NAME_REGEX.match(lastname):
        errors.append("Last name must be a valid and contain no numbers.")

    if len(errors) > 0:
        for error in errors:
            flash(error)
        return redirect ("/")
        
    else:
        query = "Insert into users(first_name, last_name, email, password, salt) values (:first_name,:last_name,:email,:hashed_pw, :salt)"
        data = {
                'first_name': request.form['first_name'],
                'last_name':  request.form['last_name'],
                'email': request.form['email'],
                'hashed_pw': hashed_pw,
                'salt': salt,
           }
        mysql.query_db(query, data)
    return redirect("/success") 

@app.route('/login', methods=["POST"])
def login():
    query1= "SELECT * from users WHERE email= :email"
    data1 = {"email":request.form["email"]}
    dbUser=mysql.query_db(query1,data1)
    if (dbUser):
        return redirect ("/welcome")
    else:
        return redirect ('/')

@app.route('/logout')
def logout():
    session.clear()
    # print "logged out"
    return redirect ('/')


#return render_template("/success.html", first_name=firstname,last_name=lastname, email=email)  #variable on left is referencing  variable in TEMPLATE page. variable on right is what we are setting the left to.
app.run(debug=True)