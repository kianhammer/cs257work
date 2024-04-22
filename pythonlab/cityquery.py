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
  sql_check_Northfield = """SELECT CASE WHEN EXISTS (
      SELECT * FROM citypop WHERE city = 'Seattle'
    )
    THEN CAST(1 AS BIT)
    ELSE CAST(0 AS BIT) END;"""
  sql_Northfield = """SELECT * FROM citypop WHERE city = 'Seattle';"""

  return cur.execute(sql_check_Northfield)
  if cur.execute(sql_check_Northfield) == 1:
    return cur.execute(sql_Northfield)
  else:
    return 'Northfield does not exist in the database'

  
  #city with largest population
  sql_city_largest_pop = """SELECT * FROM citypop ORDER BY population DESC LIMIT 1;"""

  print('City with largest population:')
  cur.execute(sql_city_largest_pop)
  

  #smallest city in Minnesota
  sql_city_smallest_minnesota = """SELECT * FROM citypop WHERE state = 'Minnesota' ORDER BY population LIMIT 1;"""

  print('Smallest city in Minnesota:')
  cur.execute(sql_city_smallest_minnesota)


  #cities furthest North/South/East/West
  sql_city_furthest_north = """SELECT * FROM citypop ORDER BY latitude DESC LIMIT 1;""";
  sql_city_furthest_south = """SELECT * FROM citypop ORDER BY latitude LIMIT 1;""";
  sql_city_furthest_west = """SELECT * FROM citypop ORDER BY longitude LIMIT 1;""";
  sql_city_furthest_east = """SELECT * FROM citypop ORDER BY longitude DESC LIMIT 1;""";

  print('Most northern city:')
  cur.execute(sql_city_furthest_north)
  print('Most southern city:')
  cur.execute(sql_city_furthest_south)
  print('Most western city:')
  cur.execute(sql_city_furthest_west)
  print('Most eastern city:')
  cur.execute(sql_city_furthest_east)


  #user input:
  stateName = input("Enter state:")
  print(stateName)
    
  


  
  conn.commit()

test_connection()
print(answer_query())
