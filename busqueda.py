from pass_manager import conexion
import psycopg2


#Busqueda para ver si el actor se encuentra en la base de datos
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

            
#Busqueda para ver si el genero se encuentra en la base de datos 
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
  
  
#Busqueda para ver si la pelicula se encuentra en la base de datos       
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
        
    
#Muestra todas las peliculas relacionadas con un actor dado 
def display_pelicula_actor(actor):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT *
                                    FROM pelicula p
                                    JOIN actor a
                                    ON p.cpelicula = a.cpelicula
                                    WHERE a.nombre Ilike '%s'"""
        cursor.execute(postgres_select_query % (actor))
        records = cursor.fetchall()
        print("\nPeliculas del actor: " + actor)
        for row in records:
            print("------------------------------")
            print("\nNombre: ", row[0], "\nDuracion: ", row[1], "\n")
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
#Muestra todas las peliculas relacionadas con un genero dado
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
        
        
def agregar_busqueda(dato):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ INSERT INTO busqueda (DATO,FECHA) VALUES ('%s',NOW()) """
        cursor.execute(postgres_select_query % (dato))
        print("\nSe ha agregado la busqueda con éxito: " + dato)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
      
#Muestra todas las peliculas relacionadas con un dato dado, este puede ser un actor, un genero o una pelicula  
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
    agregar_busqueda(dato)
        


