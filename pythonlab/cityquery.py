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

def answer_query():
  
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="hammerk",
    user="hammerk",
    password="spring997green")
  
  cur = conn.cursor()
  
  sql_check_Northfield = """SELECT CASE WHEN EXISTS (
      SELECT * FROM citypop WHERE city = 'Northfield'
    )
    THEN CAST(1 AS BIT)
    ELSE CAST(0 AS BIT) END;"""

  if cur.execute(sql_check_Northfield) == 1:
    cur.execute(sql_check_Northfield)
  else:
    print('Northfield does not exist in the database')

  sql_state_pop = """"""
    

  conn.commit()

answer_query()
