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
        return (len(records)==0, records)
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
            
def busqueda_genero(genero):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM genero WHERE nombre = '%s' """
        cursor.execute(postgres_select_query % (genero))
        records = cursor.fetchall()
        return (len(records)==0, records)
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
busqueda_actor("Will")