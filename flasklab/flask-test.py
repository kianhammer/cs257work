import flask
import psycopg2

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
    

if __name__ == '__main__':
    my_port = 5114
    app.run(host='0.0.0.0', port = my_port) 
