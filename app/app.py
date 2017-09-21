from flask import Flask
from flask import flash, render_template, request, redirect, url_for
from models import Users
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == "POST":
        user_email = request.form['inputEmail']
        user_password = request.form['inputPassword']
        if Users().login_user(user_email, user_password):
            return redirect(url_for('view_shopping_list'))
        else:
            error = "Invalid email / password!"
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == "POST":
        user_name = request.form['inputName']
        user_email = request.form['inputEmail']
        password = request.form['inputPassword']
        if Users().create_user(user_name, user_email, password) == "okay":
            return redirect(url_for('login'))
        elif Users().create_user(user_name, user_email, password) == "similar email":
            error = user_email+" is already a registered user"
        elif Users().create_user(user_name, user_email, password) == "similar name":
            error = user_name+" is already registered user"
        else:
            error = "Invalid inputs in the above fields, try again."
    return render_template("Register.html")

if __name__ == "__main__":
    app.run()
