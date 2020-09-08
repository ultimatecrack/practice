from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug import secure_filename
app = Flask(__name__)
app.debug = True
app.secret_key = 'any random string'

# @app.route('/')
# def hello_world():
#     return 'Hello World'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

# Parameter
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


@app.route('/flask')
def hello_flask():
    return 'Hello Flask'


@app.route('/python/')
def hello_python():
    return 'Hello Python'

# Url Binding Start
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
# Url Binding End


# Request type
@app.route('/userlogin')
def user_login():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
# Request type

# Template


# @app.route('/')
# def index():
#     return '<html><body><h1>Hello World</h1></body></html>'


@app.route('/')
def index():
    list1 = [1, 2, 3, 4, 5]
    return render_template('hello.html', name='Rakesh', surname=list1)


@app.route('/hello/<int:score>')
def hello_name_score(score):
    dict = [50, 60, 70]
    return render_template('hello.html', marks=dict)
# Template

# Form data to template
@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)
# Form data to template


# Cookie
@app.route('/cookie')
def cookie():
    return render_template('cookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

# Cookie

# Session
@app.route('/session')
def sessioncheck():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/loginuser'></b>" + \
        "click here to log in</b></a>"


@app.route('/loginuser', methods=['GET', 'POST'])
def loginuser():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('sessioncheck'))
    return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
	
   '''


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

# Session


#Redirect and errors
@app.route('/loginadmin')
def loginadminpage():
    return render_template('loginadmin.html')


@app.route('/loginadmin', methods=['POST'])
def loginadmin():
    if request.method == 'POST' and request.form['username'] == 'admin':
        return redirect(url_for('loginsuccess'))
    else:
        abort(401)
        return redirect(url_for('loginadminpage'))


"""
400 − for Bad Request

401 − for Unauthenticated

403 − for Forbidden

404 − for Not Found

406 − for Not Acceptable

415 − for Unsupported Media Type

429 − Too Many Requests
"""
@app.route('/success')
def loginsuccess():
    return 'logged in successfully'

#Redirect and errors


# Flash Messages
@app.route('/flashmessage')
def flashmessage():
    return render_template('flashindex.html')


@app.route('/flashmessagelogin', methods=['GET', 'POST'])
def flashmessagelogin():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('flashmessage'))
    return render_template('flashlogin.html', error=error)
# Flash Messages


# File Upload
app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['MAX_CONTENT_PATH'] = 5000


@app.route('/upload')
def upload_file_form():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

# File Upload

#Flash Mail
#!pip install Flask - Mail

# from flask import Flask
# from flask_mail import Mail, Message

# app =Flask(__name__)
# mail=Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

# @app.route("/")
# def index():
#    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
#    msg.body = "Hello Flask message sent from Flask-Mail"
#    mail.send(msg)
#    return "Sent"

#Flash Mail
def test():
    return 'This is Test'


app.add_url_rule('/test', 'test1', test)

if __name__ == "__main__":
    app.run()
