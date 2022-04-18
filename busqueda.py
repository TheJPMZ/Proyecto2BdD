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
        return (len(records)>0)
    
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

            
            
def busqueda_genero(genero):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM genero WHERE nombre_genero = '%s' """
        cursor.execute(postgres_select_query % (genero))
        records = cursor.fetchall()
        return (len(records)>0)
    
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
        
def busqueda_pelicula(pelicula):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM pelicula WHERE nombre = '%s' """
        cursor.execute(postgres_select_query % (pelicula))
        records = cursor.fetchall()
        return (len(records)>0, records)
    
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
        
        
def display_pelicula_actor(actor):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT 	NOMBRE, DURACION
                                    FROM	PELICULA
                                    INNER JOIN(	SELECT 	CPELICULA 
                                                FROM	CASTING
                                                INNER JOIN (SELECT 	CODIGO,	NOMBRE
                                                            FROM	ACTOR
                                                            WHERE	NOMBRE ILIKE '%s') A_REQUEST ON A_REQUEST.CODIGO = CASTING.CACTOR) A_CAST_REQUEST 
                                    ON	A_CAST_REQUEST.CPELICULA = PELICULA.CODIGO  """
        cursor.execute(postgres_select_query % (actor))
        records = cursor.fetchall()
        print("\nPeliculas del actor: " + actor)
        for row in records:
            print("------------------------------")
            print("\nNombre: ", row[0], "\nDuracion: ", row[1], "\n")
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
def display_pelicula_genero(genero):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT 	NOMBRE,G_REQUEST.NOMBRE_GENERO ,DURACION
                                    FROM	PELICULA
                                    INNER JOIN (SELECT 	CODIGO,	NOMBRE_GENERO
                                                FROM	GENERO
                                                WHERE	NOMBRE_GENERO ILIKE '%s') G_REQUEST ON G_REQUEST.CODIGO = PELICULA.GENERO"""
        cursor.execute(postgres_select_query % (genero))
        records = cursor.fetchall()
        print("\nPeliculas del genero: " + genero)
        for row in records:
            print("------------------------------")
            print("\nNombre: ", row[0], "\nGénero: ", row[1],"\nDuracion: ", row[2], "\n")
    
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
        
def display_cualquiera(dato):
    if busqueda_actor(dato):
        display_pelicula_actor(dato)
    elif busqueda_genero(dato):
        display_pelicula_genero(dato)
    elif busqueda_pelicula(dato)[0]:
        print("\nPelicula: " + dato)
        print("------------------------------")
        print("\nNombre: ", busqueda_pelicula(dato)[1][0][1], "\nDuracion: ", busqueda_pelicula(dato)[1][0][3], "\n")
    else:
        print("\nNo se encontró el dato: " + dato + "\n")
        

display_cualquiera('Accion')

