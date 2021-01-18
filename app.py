
from flask import render_template, redirect
from flask import request, session
from flask import Flask, url_for, flash, blueprints

import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)



@app.route("/")
def home():
    return render_template('MyCVHomePage.html')


@app.route("/userlist")
def userlist():
    return render_template('USERLIST.html')


@app.route("/stayintouch")
def stayintouch():
    return render_template('Stay In touch.html')


@app.route("/recommendation")
def recommendation():
    return render_template('Recommendation.html')


@app.route("/8")
def assignment8():
    return render_template('Assigment8.html',
                           user={'firstname': "Ziv", 'lastname': "Bach"},
                           Hobbies=['Be With Friends', 'Shopping', 'Go To the Beach', 'Listen to Music', 'Eat good Food'])


@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9():
    email = ''
    username = ''
    flag = False
    if 'name' in request.args:
        flag = True
        username = request.args['username']
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        session['loggedIn'] = True
        session['username'] = username

    users = [{'firstname': 'Hadar', 'lastname': 'Biton', 'email': 'hb@gmail.com', 'username': 'hadarb'},
                {'firstname': 'David', 'lastname': 'Yehoda', 'email': 'dh@gmail.com', 'username': 'davidy'},
                {'firstname': 'Tal', 'lastname': 'Baril', 'email': 'tb@gmail.com', 'username': 'talb'},
                 {'firstname': 'Rachel', 'lastname': 'Gotlibe', 'email': 'rg@gmail.com', 'username': 'rachelg'}]

    return render_template('assignment9.html',
                           request_methods=request.method,
                           username=username, email=email, users=users, flag=flag)



@app.route('/logout')
def sign_out():
    session.pop('username')
    session['loggedIn'] = False
    return redirect('/assignment9')



from assigment10.assigment10 import assigment10
app.register_blueprint(assigment10)



# run the application
if __name__ == "__main__":
    app.run(debug=True)
