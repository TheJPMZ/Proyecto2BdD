import psycopg2
import random
import datetime
from pass_manager import conexion


def executequery(p_cursor, p_query, parameters=None):
    try:
        if parameters:
            p_cursor.execute(p_query % parameters)
        else:
            p_cursor.execute(p_query)
    except psycopg2.Error as e:
        print("Ocurrio un error: ", e)
        exit()
    return p_cursor

connection = conexion()
cursor = connection.cursor()

query1 = """SELECT cperfil FROM Perfil"""

executequery(cursor, query1)
result = cursor.fetchall()

profile = random.choice(result)

query2 = """SELECT cpelicula FROM Pelicula"""

executequery(cursor, query2)
result = cursor.fetchall()

movie = random.choice(result)

query3 = """SELECT duracion FROM Pelicula WHERE cpelicula = '%s'"""

executequery(cursor,query3,movie[0])
result = cursor.fetchall()

duration = result[0]

if random.randint(0,1):
    duration = int(duration[0])
else:
    duration = random.randint(0,*duration)

insert_query = """INSERT INTO ver (cperfil, cpelicula, duracion, fecha, timestmp) VALUES ('%s','%s','%s',Now(),Now())"""

executequery(cursor,insert_query,(*profile,*movie,duration))

connection.commit()

