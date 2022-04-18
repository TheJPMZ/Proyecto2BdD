from pass_manager import conexion
import psycopg2


#Busqueda para recopilar todas las peliculas de un actor.
def busqueda_actor(actor):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM actor WHERE nombre = '%s' """
        cursor.execute(postgres_select_query % (actor))
        records = cursor.fetchall()
        for row in records:
            print("Nombre: ", row[1])
            print("Apellido: ", row[2])
            print("\n")
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
busqueda_actor("Will")