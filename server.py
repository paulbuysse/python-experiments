from flask import Flask
from flask import request
# import psycopg2
import psycopg2

app = Flask(__name__)
app.config["DEBUG"] = True

try:
    connection = psycopg2.connect(
        user = "Paul",
        password = Null,
        host = "localhost",
        port = "5000",
        database = "fs-redux-books"
    )

@app.route('/')
def hello_paul():
    return 'Hello, Paul!'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/food/<selected_food>', methods=['GET', 'POST', 'PUT'])
def food_req(selected_food):
    if request.method == 'POST':
        return post_that_food(selected_food)
    elif request.method == 'PUT':
        return put_function()
    elif request.method == 'GET':
        return get_dishes()
    else:
        return no_food_today()

def post_that_food(this_food):
    this_var = this_food
    return this_var

def put_function():
    return 'putting food and stuff'

def no_food_today():
    return 'no food posted'

def get_dishes():
    conn = psycopg2.connect(dbname='fs-redux-books')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    # conn = psycopg2.connect("menus_plus=test user=postgres")
    # cur = conn.cursor()

    # cur.execute("SELECT * FROM dishes;")
    # cur.fetchone()

    # cur.close()
    # conn.close()