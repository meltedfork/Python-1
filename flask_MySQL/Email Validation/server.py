from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key= "12345"

mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():
    print
    return render_template('index.html')

@app.route('/validate', methods = ["POST"])
def validate():
    query = "SELECT * from emails WHERE address = :address"
    data = {"address": request.form["email"] }
    databaseEmail = mysql.query_db(query,data)
    print databaseEmail
    if (databaseEmail):
        flash("Success!")
    else:
        flash("Email not in database")
    return redirect('/')
    

app.run(debug=True)