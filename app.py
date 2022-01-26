from flask import Flask, render_template, request, redirect, flash, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key'

connection = psycopg2.connect(host='localhost', user='postgres', password='yourPassword', database='users')
cursor = connection.cursor()

@app.route("/")
def home():
    if ("user" in session):
        return redirect("/welcome")
    else:
        return render_template("index.html")

@app.route("/login")
def login():
    if ("user" in session):
        return redirect("/welcome")
    else:
        return render_template("login.html")

@app.route("/welcome")
def welcome():
    if ("user" in session):
        return render_template("welcome.html")
    else:
        return redirect("/login")

@app.route("/handlesignup", methods=["GET", "POST"])
def handlesignup():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pass1")
        cpassword = request.form.get("pass2")

        cursor.execute("SELECT * FROM users WHERE username=%s", [username])
        user = cursor.fetchall()

        if len(username) < 4 or len(username) > 12:
            flash("Username must contain characters between 4 and 12", "danger")
            return redirect("/")
        elif not username.isalnum() or username.isnumeric():
            flash("Username can only contain letters and numbers", "danger")
            return redirect("/")
        elif len(user) > 0:
            flash("This username already exists", "danger")
            return redirect("/")
        elif len(password) < 6:
            flash("Password must contain atleast 8 characters", "danger")
            return redirect("/")
        elif password.isalpha() or password.isnumeric():
            flash("Password cannot contain only letters or only numbers", "danger")
            return redirect("/")
        elif (password!= cpassword):
            flash("Both password and confirm password should match", "danger")
            return redirect("/")
        else:
            hashed_pass = generate_password_hash(password, method='sha256')
            cursor.execute("INSERT INTO users (username, password, timestamp) VALUES (%s, %s, %s)", (username, hashed_pass, datetime.now()))
            connection.commit()
            flash("Your account has been successfully created", "success")
            return redirect("/login")
    else:
        return "<h1>Bad Request (400)</h1>"

@app.route("/handlelogin", methods=["GET", 'POST'])
def handlelogin():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("password")

        cursor.execute("SELECT * FROM users WHERE username=%s", [username])
        user = cursor.fetchone()

        if len(user) > 0:
            # Verify the user's hashed password
            if check_password_hash(user[2], password):
                session["user"] = username
                flash("You have been successully logged in", "success")
                return redirect("/welcome")
            else:
                flash(f"Invalid password! Please try again")
                return redirect("/login")
        else:
            flash("No such user exists with that username")
            return redirect("/login")
    else:
        return "<h1>Bad Request (400)</h1>"

@app.route("/logout")
def handlelogout():
    if ("user" in session):
        session.pop("user")
        flash("You have been successfully logged out", "success")
        return redirect("/login")
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)