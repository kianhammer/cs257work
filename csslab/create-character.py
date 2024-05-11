import flask
import psycopg2
from flask import render_template
import random

app = flask.Flask(__name__)

@app.route('/')
def welcome():


  return render_template("character.html")



if __name__ == '__main__':
    my_port = 5114
    app.run(host='0.0.0.0', port = my_port) 
