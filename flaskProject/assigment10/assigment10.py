from flask import Blueprint, render_template
from flask import request, session
from flask import Flask, redirect,  flash
import mysql.connector

assigment10 = Blueprint('assigment10', __name__, static_folder='static', static_url_path='/assigment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                        passwd='root',
                                        database='WEB_EX_10')
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
        query = "INSERT INTO users(firstname, lastname, Email) VALUES ('%s', '%s', '%s')" % (firstname, lastname, email)
        interact_db(query, query_type='commit')

    if request.method == 'GET':
        if 'firstnameUp' in request.args:
            firstname = request.args['firstnameUp']
            emailUp = request.args['emailUp']
            query = "UPDATE users SET Email = '%s' WHERE firstname = '%s' " % (emailUp, firstname)
            interact_db(query, query_type='commit')

        if 'firstnameDel' in request.args:
            firstname = request.args['firstnameDel']
            query = "DELETE FROM users WHERE firstname = '%s';" % firstname
            interact_db(query, query_type='commit')

    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')

    return render_template('assigment10.html', users=query_result)
