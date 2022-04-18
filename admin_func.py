from pass_manager import conexion
import psycopg2




def top10_generos():
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT GENERO,COUNT(GENERO)
                                    FROM GENERO
                                    NATURAL JOIN VER
                                    GROUP BY GENERO"""
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        print("\nTop 10 generos vistos: ")
        print("----------------------------------------------------")
        for row in records:
            print("\nGenero: " + row[0], " | Cantidad vista: " + str(row[1]))
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
  
    
def minutos_consum(fecha1, fecha2):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT	SUM(DURACION)
                                    FROM	VER
                                    WHERE FECHA>='%s' 
                                    AND fecha <= '%s' """
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        print("\nMinutos consumidos: " + str(records[0][0]))
        

    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def rep_categoria():
    connection = conexion()
    
def rep_cuenta(fecha1,fecha2):
    connection = conexion()
    
def cant_cuentas():
    connection = conexion()
    
def top10_actores():
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT ACTOR.NOMBRE, COUNT(ACTOR)
                                    FROM ACTOR
                                    INNER JOIN(	SELECT *
                                                FROM	PERFIL
                                                NATURAL JOIN 	USUARIO
                                                NATURAL JOIN	VER
                                                WHERE	CUENTA ILIKE 'Avanzada' 
                                                OR 		CUENTA ILIKE 'Estandar') VUP_SUB 
                                    ON VUP_SUB.CPELICULA = ACTOR.CPELICULA
                                    GROUP BY ACTOR.NOMBRE
                                    ORDER BY ACTOR.NOMBRE DESC
                                    LIMIT 10"""
                                    
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        print("\nTop 10 actores más vistos: ")
        print("----------------------------------------------------")
        for row in records:
            print("\nActor: " + row[0], " | Cantidad vista: " + str(row[1]))
            
            
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)




def top10_directores():
    connection = conexion()
    
def hora_pico(fecha):
    connection = conexion()
    

top10_generos()


''' INSERT INTO VER(
	cperfil, cpelicula, DURACION, FECHA)
VALUES (
	'Per1','P7', 45, NOW())
; '''