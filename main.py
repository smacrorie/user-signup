from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def signup():
    return render_template('signup.html')

@app.route('/', methods = ['POST'])
def validate_signup():
    username_error = ''
    password_error = ''
    verifypassword_error = ''
    email_error = ''
   

    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    # 
    if username == "" and password == '' and verifypassword == '':
        username_error = "Please type a username"
        password_error = "Please type a password"
        verifypassword_error = "Please verify your password"
        return render_template('signup.html', username_error = username_error, password_error = password_error,
            verifypassword_error = verifypassword_error)
    elif len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "That's not a valid username"
        return render_template('signup.html', username_error = username_error)        
        
    if  password == '' and verifypassword == '':       
        password_error = "Please type a password"
        verifypassword_error = "Please verify your password"
        return render_template('signup.html',password_error = password_error,
            verifypassword_error = verifypassword_error, username = username)
    elif len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "That's not a valid password"
        return render_template('signup.html', password_error = password_error, username = username)         

    # if verify password box is left blank or it doesn't match the password box then display error message
    if  verifypassword == '' or verifypassword != password:    
        verifypassword_error = "Passwords don't match"
        return render_template('signup.html',verifypassword_error = verifypassword_error, username = username)

    if email != "":
        if len(email) < 3  or len(email) > 20 or ' ' in email or '@' not in email or '.' not in email:
            email_error = "Please enter a valid email" 
            return render_template('signup.html', email_error = email_error, verifypassword_error = verifypassword_error,
                password_error = password_error, username_error = username_error,username = username, password = password,
                verifypassword = verifypassword)     

    return redirect('/welcome?username=' + username)     

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)   


app.run()
