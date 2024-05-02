import flask
import psycopg2
from flask import render_template
import random

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:rgb(170, 120, 20)">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    number = int(num1) + int(num2)
    return '' + str(number)

@app.route('/pop/<abbrev>')
def my_pop(abbrev):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="hammerk",
        user="hammerk",
        password="spring997green")
    
    cur = conn.cursor()

    sql_state = """SELECT * FROM statepop WHERE code = %s;"""
    cur.execute(sql_state, [abbrev])
    state = cur.fetchone()

    return str(state[2])

@app.route('/random-person')
def my_randomPerson():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="hammerk",
        user="hammerk",
        password="spring997green")
    
    cur = conn.cursor()

    sql_city = """SELECT * FROM citypop ORDER BY RANDOM() LIMIT 1;"""

    nameList = ["Bob", "Alice", "Carl", "Samantha", "Dave", "John", "Sarah", "Becca", "Cameron", "Chloe", "Eric", "Alex", "Tony", "Stephanie", "Tiffany", "Britney", "Max", "Tom", "Jerry", "Isabella"]
    adjectiveList = ["Wise", "Great", "Pure", "Brave", "Mighty", "Rich", "Bold", "Lucky", "Curious", "Kind"]
    cur.execute(sql_city)
    city = cur.fetchone()[0]
    adjective = adjectiveList[random.randint(0,9)]
    name = nameList[random.randint(0,19)]
    
    person = name + " the " + adjective + " was born in " + city + " in " + str(random.randint(1700, 2024))

    return render_template("person.html", randomPerson = person)

@app.route('/person')
def my_person():
    return render_template("title.html")

if __name__ == '__main__':
    my_port = 5114
    app.run(host='0.0.0.0', port = my_port) 
