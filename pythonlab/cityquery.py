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

  #search for Northfield
  sql_Northfield = """SELECT * FROM citypop WHERE city = 'Northfield';"""

  cur.execute(sql_Northfield)
  northfield = cur.fetchone()
  if northfield == None:
    print('Northfield does not exist in the database')
  else:
    print(northfield)
  
  #city with largest population
  sql_city_largest_pop = """SELECT * FROM citypop ORDER BY population DESC LIMIT 1;"""

  print('City with largest population:')
  cur.execute(sql_city_largest_pop)
  print(cur.fetchone())

  #smallest city in Minnesota
  sql_city_smallest_minnesota = """SELECT * FROM citypop WHERE state = 'Minnesota' ORDER BY population LIMIT 1;"""

  print('Smallest city in Minnesota:')
  cur.execute(sql_city_smallest_minnesota)
  print(cur.fetchone())


  #cities furthest North/South/East/West
  sql_city_furthest_north = """SELECT * FROM citypop ORDER BY latitude DESC LIMIT 1;""";
  sql_city_furthest_south = """SELECT * FROM citypop ORDER BY latitude LIMIT 1;""";
  sql_city_furthest_west = """SELECT * FROM citypop ORDER BY longitude LIMIT 1;""";
  sql_city_furthest_east = """SELECT * FROM citypop ORDER BY longitude DESC LIMIT 1;""";

  print('Most northern city:')
  cur.execute(sql_city_furthest_north)
  print(cur.fetchone())
  
  print('Most southern city:')
  cur.execute(sql_city_furthest_south)
  print(cur.fetchone())
  
  print('Most western city:')
  cur.execute(sql_city_furthest_west)
  print(cur.fetchone())
  
  print('Most eastern city:')
  cur.execute(sql_city_furthest_east)
  print(cur.fetchone())


  #user input:
  stateName = input("Enter state:")
  
  sql_state_list = """SELECT * FROM statepop;"""
  cur.execute(sql_state_list)
  state_list = cur.fetchall()

  for state in state_list:
    print(state[0])
    if stateName == 'MN':
      print(state[1])
    
  


  
  conn.commit()

test_connection()
answer_query()
