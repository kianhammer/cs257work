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
    print(northfield[0])
  
  #city with largest population
  sql_city_largest_pop = """SELECT * FROM citypop ORDER BY population DESC LIMIT 1;"""

  print('City with largest population:')
  cur.execute(sql_city_largest_pop)
  print(cur.fetchone()[0])

  #smallest city in Minnesota
  sql_city_smallest_minnesota = """SELECT * FROM citypop WHERE state = 'Minnesota' ORDER BY population LIMIT 1;"""

  print('Smallest city in Minnesota:')
  cur.execute(sql_city_smallest_minnesota)
  print(cur.fetchone()[0])


  #cities furthest North/South/East/West
  sql_city_furthest_north = """SELECT * FROM citypop ORDER BY latitude DESC LIMIT 1;""";
  sql_city_furthest_south = """SELECT * FROM citypop ORDER BY latitude LIMIT 1;""";
  sql_city_furthest_west = """SELECT * FROM citypop ORDER BY longitude LIMIT 1;""";
  sql_city_furthest_east = """SELECT * FROM citypop ORDER BY longitude DESC LIMIT 1;""";

  print('Most northern city:')
  cur.execute(sql_city_furthest_north)
  print(cur.fetchone()[0])
  
  print('Most southern city:')
  cur.execute(sql_city_furthest_south)
  print(cur.fetchone()[0])
  
  print('Most western city:')
  cur.execute(sql_city_furthest_west)
  print(cur.fetchone()[0])
  
  print('Most eastern city:')
  cur.execute(sql_city_furthest_east)
  print(cur.fetchone()[0])


  #user input:
  stateName = input("Enter state:")
  
  sql_state_list = """SELECT * FROM statepop WHERE code = %s;"""
  cur.execute(sql_state_list, [stateName])
  state_abbreviation = cur.fetchone()

  if state_abbreviation != None:
    stateName = state_abbreviation[1]

  sql_cities_in_state = """SELECT * FROM citypop WHERE state = %s;"""
  cur.execute(sql_cities_in_state, [stateName])
  city_list = cur.fetchall()
  totalPopulation = 0
  for city in city_list:
    totalPopulation = totalPopulation + int(city[2])

  print('Total Population In The State ' + stateName + ':')
  print(totalPopulation)
    
  

test_connection()
answer_query()
