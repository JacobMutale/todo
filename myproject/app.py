from markupsafe import escape
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def index(user = None, todos=[]):
    if request.method == 'POST':
        return 'add todo'
    elif request.method == 'PUT':
        return 'edit todo'
    elif request.method == 'DELETE':
        return 'delete todo'
    else:
        # you can also pass in a argument like this
        # render_template('index.html', todos = todos, user = user)
        return render_template('index.html', user= user, todos=todos)

@app.route("/login", methods= ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return 'get login credentials'
    else:
        return render_template('login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return 'register user'
    else:
        return render_template('login.html')

@app.route("/todo/<int:id>", methods=['GET'])
def show_todo(id):
    return render_template('login.html')



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