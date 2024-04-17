import psycopg2

def test_connection():

  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="hammerk",
    user="hammerk",
    password="spring997green")
  
  if conn is not None:
    print("Connection Worked!")
  else:
    print("Problem With Connection")
    
  return None

def create_tables():
  
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="hammerk",
    user="hammerk",
    password="spring997green")
  
  cur = conn.cursor()
  

sql_city_pop = """DROP TABLE IF EXISTS cityPop;
  CREATE TABLE cityPop (
    city char(40),
    state char(20),
    population int,
    latitude real,
    longitude real
  );"""

sql_state_pop = """DROP TABLE IF EXISTS statePop;
  CREATE TABLE statePop (
    code char(3),
    state char(20),
    population int
  );"""
    
  cur.execute( sql_city_pop )
  cur.execute( sql_state_pop )
