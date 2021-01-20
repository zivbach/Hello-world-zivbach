from flask import Blueprint, render_template
from flask import request, session
from flask import Flask, redirect,  flash
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

assigment10 = Blueprint('assigment10', __name__, static_folder='static', static_url_path='/assigment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                        passwd='root',
                                        database='Ex_10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assigment10.route('/assigment10', methods=['GET', 'POST'])
def assi10():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        username = request.form['username']
        query = "INSERT INTO users(username, firstname, lastname, email) VALUES ('%s', '%s', '%s', '%s')" % (firstname, lastname, email, username)
        interact_db(query, query_type='commit')

    if request.method == 'GET':
        if 'usernameUpload' in request.args:
            firstname = request.args['usernameUpload']
            emailUp = request.args['emailUpload']
            query = "UPDATE users SET Email = '%s' WHERE username = '%s' " % (emailUp, username)
            interact_db(query, query_type='commit')

        if 'firstnameDel' in request.args:
            firstname = request.args['usernameDelete']
            query = "DELETE FROM users WHERE username = '%s';" % username
            interact_db(query, query_type='commit')

    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')

    return render_template('assigment10.html', users=query_result)
