from markupsafe import escape
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
# TODO: call to database operations
def index(user = None, todos=[]):
    if request.method == 'POST':
        if valid_todo(request.form['title'], request.form['content']):
            return 'add todo'
        else:
            return 'the todo is not complete'
    elif request.method == 'PUT':
        if todo_exisits(request.form['id']):
            return 'edit todo'
        else:
            return 'todo does not exisit'
    elif request.method == 'DELETE':
        if todo_exisits(request.form['id']):
            return 'delete todo'
        else:
            return 'Todo does not exisit'
    else:
        # you can also pass in a argument like this
        # render_template('index.html', todos = todos, user = user)
        return render_template('index.html', user= user, todos=todos)

@app.route("/login", methods= ['GET', 'POST'])
def signin():
    # TODO: save user in a db and return user redirect them to the '/'
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            print('SUCCESS')
            return 'SUCCESS'  
        else:
            return 'Invalid username/password'
    else:
        return render_template('login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return 'register user'
        else:
            return 'not a valid'
    else:
        return render_template('signup.html')

@app.route("/todo/<int:id>", methods=['GET'])
def show_todo(id, todo = None):
    return render_template('todo.html', todo=todo)


def valid_login(username, password):
    # TODO: data base operations
    if username != '' and password != '':
        return True
    else:
        return False

def valid_todo(title, content):
    # TODO: data base operations
    if title != '' and content != '':
        return True
    else:
        return False

def todo_exisits(id):
    # TODO: data base operations
    if id != '':
        return True
    else:
        return False

# you can use url_for() to build urls for a specific function it takes the name of the function
# as it's first argument and any number of keyword arguements 
with app.test_request_context():
    print(url_for('index'))
    print(url_for('signin'))
    print(url_for('signin', next='/'))
    print(url_for('signup'))
    print(url_for('show_todo', id='1'))
    print(url_for('static', filename='style.css'))




@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"