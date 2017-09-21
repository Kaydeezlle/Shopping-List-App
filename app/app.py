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

if __name__ == "__main__":
    app.run()
