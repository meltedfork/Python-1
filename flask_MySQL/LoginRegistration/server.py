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
    if "user_id" in session:                #if there is a user already logged in, go to welcome template
        return redirect("/welcome")
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/register', methods = ["POST"])
def register():
    
    errors = []     #empty errors list to flash after all/errors found
    firstname = request.form["first_name"]      #variable firstname is whatever put into text field for first name
    lastname = request.form["last_name"]
    email=request.form["email"]
    password=request.form["password"]
    salt =  binascii.b2a_hex(os.urandom(15))    # salt variable. randomizes 15 characters in this case.
    hashed_pw = md5.new(password + salt).hexdigest() #setting new variable that is a salted and hashed password variation
    confirm=request.form["confirm"]


    if len(firstname) < 2:
       errors.append("First name field must be more than 2 letters!")
    
    if len(email) < 1:
        errors.append("Email field cannot be empty!")

    if len(lastname) < 2:
        errors.append("Last name field must be more than 2 letters!")
    
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

    if len(errors) > 0:     #if any errors found, flash them
        for error in errors:    #loop through all errors in error list
            flash(error)    #flash each error
        return redirect ("/")
        
    else:
        query = "Insert into users(first_name, last_name, email, password, salt) values (:first_name,:last_name,:email,:hashed_pw, :salt)"  # run query to insert into users table the values from the below data
        data = {    
                'first_name': request.form['first_name'],
                'last_name':  request.form['last_name'],
                'email': request.form['email'],
                'hashed_pw': hashed_pw,
                'salt': salt,
           }
        newUser=mysql.query_db(query,data)  #the newuser is set to be the below query
        mysql.query_db(query, data)         #run the query to assign the values to the new user and give him a dictionary 
        session["user_id"] = ['id']         #set session for the new user
        return redirect("/success") 

@app.route('/login', methods=["POST"])
def login():
    query1= "SELECT * from users WHERE email= :email"   #select all from table USERS where the email column is equal to the input email from form
    data1 = {"email":request.form["email"]}             #at the key value EMAIL, assign value of the input email
    dbUser=mysql.query_db(query1,data1)                 #the db user gets all his dictionary values assigned
    if (dbUser):                                        #if it is a valid user
        session["user_id"] = dbUser[0]['id']            #assign him a session id
        return redirect ("/welcome")
    else:
        return redirect ('/')

@app.route('/logout')
def logout():
    session.clear()             #clear the session
    return redirect ('/')

@app.route('/thewall')
def thewall():
    return render_template("thewall.html")


#return render_template("/success.html", first_name=firstname,last_name=lastname, email=email)  #variable on left is referencing  variable in TEMPLATE page. variable on right is what we are setting the left to.
app.run(debug=True)