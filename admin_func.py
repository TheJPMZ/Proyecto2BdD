from email.mime import message

import pass_manager
import simulacion
from pass_manager import conexion
import psycopg2
from registro import Registro
from registro import Profiler




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
        cursor.execute(postgres_select_query % (fecha1, fecha2))
        records = cursor.fetchall()
        print("\nMinutos consumidos: " + str(records[0][0]))
        

    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def rep_categoria(fecha1, fecha2):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT 		CLASIFICACION, COUNT(*) AS C_CLAS
                                    FROM		VER
                                    INNER JOIN	PELICULA ON PELICULA.CPELICULA = VER.CPELICULA
                                    WHERE       VER.FECHA >= '%s'
                                    AND         VER.FECHA <= '%s'
                                    GROUP BY 	CLASIFICACION
                                    ORDER BY	C_CLAS DESC"""
        cursor.execute(postgres_select_query % (fecha1, fecha2))
        records = cursor.fetchall()
        print("\nReproducciones por categoria: ")
        print("----------------------------------------------------\n")
        for row in records:
            print("Categoria: " + row[0], " | Reproducciones: " + str(row[1]))

    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
    
def rep_cuenta(fecha1,fecha2):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT 		CUSUARIO, COUNT(*) AS C_CLAS
                                    FROM		VER
                                    INNER JOIN	PERFIL ON PERFIL.CPERFIL = VER.CPERFIL
                                    WHERE       VER.FECHA >= '%s'
                                    AND         VER.FECHA <= '%s'
                                    GROUP BY 	CUSUARIO
                                    ORDER BY	C_CLAS DESC"""
        cursor.execute(postgres_select_query % (fecha1, fecha2))
        records = cursor.fetchall()
        print("\nReproducciones por cuenta: ")
        print("----------------------------------------------------\n")
        for row in records:
            print("Cuenta: " + row[0], " | Reproducciones: " + str(row[1]))

    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
    
def cant_cuentas():
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT 	COUNT(*)
                                    FROM	USUARIO
                                    WHERE	USUARIO.DATE >= (USUARIO.DATE - INTERVAL '6 months') 
                                    AND USUARIO.CUENTA ILIKE 'Avanzada'"""
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        print("\nCantidad de cuentas creadas en los ultimos 6 meses: " + str(records[0][0]))
        

    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
    
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
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT DIRECTOR, COUNT(DIRECTOR)
                                    FROM PELICULA
                                    INNER JOIN(	SELECT *
                                                FROM	PERFIL
                                                NATURAL JOIN 	USUARIO
                                                NATURAL JOIN	VER
                                                WHERE	CUENTA ILIKE 'Avanzada' 
                                                OR 		CUENTA ILIKE 'Estandar') VUP_SUB 
                                    ON VUP_SUB.CPELICULA = PELICULA.CPELICULA
                                    GROUP BY DIRECTOR
                                    ORDER BY DIRECTOR DESC"""
                                    
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        print("\nTop 10 directores más vistos: ")
        print("----------------------------------------------------")
        for row in records:
            print("\nDirector: " + row[0], " | Cantidad vista: " + str(row[1]))
            
            
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)


def top10_busqueda():
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT *
                                    FROM TOP10BUSQUEDA"""

        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        print("\nTop 10 busquedas más hechas: ")
        print("----------------------------------------------------")
        for row in records:
            print("\nBusqueda: " + row[0], " | Cantidad: " + str(row[1]))
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def top5_admins(fecha1,fecha2):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT *
                                    FROM TOP5ADMINS('%s','%s')"""

        cursor.execute(postgres_select_query % (fecha1, fecha2))
        records = cursor.fetchall()
        print("\nTop 5 ADMINS CON MAS MODIFICACIONES: ")
        print("----------------------------------------------------")
        for row in records:
            print("\aAdmin: " + row[0], " | Cantidad: " + str(row[1]))
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)
        
def top20_noterminadas(fecha1,fecha2):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT *
                                    FROM PELICULAS_NOVISTAS('%s','%s')"""

        cursor.execute(postgres_select_query % (fecha1, fecha2))
        records = cursor.fetchall()
        print("\nTop 20 PELICULAS NO TERMINADAS: ")
        print("----------------------------------------------------")
        for row in records:
            print("\PELICULA: " + row[0], " | Cantidad: " + str(row[1]))
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def top5_mes_horas(mes):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT *
                                    FROM top5_mes_horas(%s)
                                    ORDER BY HOURS ASC, CANTI DESC"""

        cursor.execute(postgres_select_query % (str(mes)))
        records = cursor.fetchall()
        print("\nTop 5 peliculas por cada hora para el mes seleccionado: ")
        print("----------------------------------------------------")
        for row in records:
            print("\Hora: " + str(row[0]), " | PELICULA: " + str(row[1]) + " | Cantidad: " + str(row[2]))
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)



def agregar_anunciante(canuncio, anuncio,anunciante):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ INSERT INTO anuncios(canuncio, anuncio, anunciante)
                                    VALUES ('%s','%s','%s')"""

        cursor.execute(postgres_select_query % (canuncio, anuncio,anunciante))
        connection.commit()
        print("\nAnunciante agregado con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def agregar_pelicula(cpelicula, nombre, duracion, clasificacion, imagen, link, director):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ INSERT INTO PELICULA(cpelicula, nombre, duracion, clasificacion, imagen, link, director)
                                    VALUES ('%s','%s','%f','%d','%s','%s','%s')"""

        cursor.execute(postgres_select_query % (cpelicula, nombre, duracion, clasificacion, imagen, link, director))
        connection.commit()
        print("\nPelicula agregada con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)


def agregar():
    opcion1 = ''
    print("\nMENU DE AGREGAR:")
    print("1. PELICULA")
    print("2. ANUNCIANTE")
    print("3. VOLVER")
    opcion1 = input("\nIngrese una opcion: ")
    if opcion1 == '1':
        cpelicula = input("\nIngrese el codigo de la pelicula: ")
        nombre = input("\nIngrese el nombre de la pelicula: ")
        duracion = float(input("\nIngrese la duracion de la pelicula: "))
        clasificacion = int(input("\nIngrese la clasificacion de la pelicula: "))
        imagen = input("\nIngrese el link de la imagen de la pelicula: ")
        link = input("\nIngrese el link de la pelicula: ")
        director = input("\nIngrese el director de la pelicula: ")
        agregar_pelicula(cpelicula, nombre, duracion, clasificacion, imagen, link, director)
    elif opcion1 == '2':
        canuncio = input("\nIngrese el codigo del anuncio: ")
        anuncio = input("\nIngrese el anuncio: ")
        anunciante = input("\nIngrese el anunciante: ")
        agregar_anunciante(canuncio, anuncio,anunciante)
    elif opcion1 == '3':
        print("\nVOLVIENDO...")
    else:
        print("\nOpcion invalida")

def modificar_pelicula(columna, newvalue, cpelicula):
    try:
        connection = conexion()
        cursor = connection.cursor()

        postgres_select_query = """UPDATE PELICULA
                                    SET %s = '%s'
                                    WHERE cpelicula = '%s'"""

        cursor.execute(postgres_select_query % (columna,newvalue,cpelicula))
        connection.commit()
        print("\nPeliculada cambiada con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)


def modificar_anunciante(columna, newvalue,canuncio):
    try:
        connection = conexion()
        cursor = connection.cursor()

        postgres_select_query = """UPDATE ANUNCIO
                                    SET %s = '%s'
                                    WHERE canunciante = '%s'"""

        cursor.execute(postgres_select_query % (columna,newvalue,canuncio))
        connection.commit()
        print("\nPeliculada cambiada con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def modificar_usuario(columna, newvalue,cusuario):
    try:
        connection = conexion()
        cursor = connection.cursor()

        postgres_select_query = """UPDATE USUARIO
                                    SET %s = '%s'
                                    WHERE cusuario = '%s'"""

        cursor.execute(postgres_select_query % (columna,newvalue,cusuario))
        connection.commit()
        print("\nPeliculada cambiada con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)


def modificar():
    opcion1 = ''
    print("\nMENU DE MODIFICAR:")
    print("1. USUARIO")
    print("2. ANUNCIANTE")
    print("3. PELICULA")
    print("4. VOLVER")
    opcion1 = input("\nIngrese una opcion: ")
    if opcion1 == '1':
        columna =  input("\nIngrese la columna a modificar: ")
        cusuario = input("\nIngrese el codigo del usuario para modificar: ")
        newvalue = input("\nIngrese el nuevo valor: ")
        modificar_usuario(columna, newvalue,cusuario)

    elif opcion1 == '2':
        columna =  input("\nIngrese la columna a modificar: ")
        canuncio = input("\nIngrese el codigo del anuncio para modificar: ")
        newvalue = input("\nIngrese el nuevo valor: ")
        modificar_anunciante(columna, newvalue,canuncio)


    elif opcion1 == '3':
        columna =  input("\nIngrese la columna a modificar: ")
        cpelicula = input("\nIngrese el codigo del anuncio para modificar: ")
        newvalue = input("\nIngrese el nuevo valor: ")
        modificar_pelicula(columna, newvalue,cpelicula)
    elif opcion1 == '4':
        print("\nVOLVIENDO...")
    else:
        print("\nOpcion invalida")


def eliminar_usuario(cusuario):
    try:
        connection = conexion()
        cursor = connection.cursor()

        postgres_select_query = """DELETE FROM USUARIO
                                    WHERE CUSUARIO = '%s';"""

        cursor.execute(postgres_select_query % cusuario)
        connection.commit()
        print("\nUsuario eliminado con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def eliminar_anunciante(canuncio):
    try:
        connection = conexion()
        cursor = connection.cursor()

        postgres_select_query = """DELETE FROM ANUNCIO
                                    WHERE CANUNCIO = '%s';"""

        cursor.execute(postgres_select_query % canuncio)
        connection.commit()
        print("\nUsuario eliminado con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def eliminar_pelicula(cpelicula):
    try:
        connection = conexion()
        cursor = connection.cursor()

        postgres_select_query = """DELETE FROM PELICULA
                                    WHERE CPELICULA = '%s';"""

        cursor.execute(postgres_select_query % cpelicula)
        connection.commit()
        print("\nUsuario eliminado con exito")
    except (Exception, psycopg2.Error) as error:
        print("\nError while fetching data from PostgreSQL", error)

def eliminar():
    opcion1 = ''
    print("\nMENU DE ELIMINAR:")
    print("1. USUARIO")
    print("2. ANUNCIANTE")
    print("3. PELICULA")
    print("4. VOLVER")
    opcion1 = input("\nIngrese una opcion: ")
    if opcion1 == '1':
        cusuario = input("\nIngrese el codigo del usuario para eliminar: ")
        eliminar_usuario(cusuario)

    elif opcion1 == '2':
        canuncio = input("\nIngrese el codigo del anuncio para eliminar: ")
        eliminar_anunciante(canuncio)

    elif opcion1 == '3':
        cpelicula = input("\nIngrese el codigo de la pelicula para eliminar: ")
        eliminar_pelicula(cpelicula)
    elif opcion1 == '4':
        print("\nVOLVIENDO...")
    else:
        print("\nOpcion invalida")



def alterar_registros():
    opcion1 = ''
    while opcion1 != '4':
        print("\nMENU DE MODIFICACIONES:")
        print("1. Agregar")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Volver")
        opcion1 = input("\nIngrese una opcion: ")
        if opcion1 == '1':
            agregar()
        elif opcion1 == '2':
            modificar()
        elif opcion1 == '3':
            eliminar()
        elif opcion1 == '4':
            print("\nVolviendo...")
        else:
            print("\nOpcion invalida")



def mainloop():
    opcion = ''
    fecha1 = ''
    fecha2 = ''
    while opcion != '15':
        print("\nMENU:")
        print("1. Top 10 generos vistos")
        print("2. Minutos consumidos")
        print("3. Reproducciones por categoría")
        print("4. Reproducciones por cuenta")
        print("5. Cantidad de cuentas creadas en los ultimos 6 meses")
        print("6. Top 10 actores más vistos")
        print("7. Top 10 directores más vistos")
        print("8. Top 10 busquedas")
        print("9. Top 5 admins con mas cambios")
        print("10. Top 20 peliculas no terminadas de ver")
        print("11. Crear nuevo administrador")
        print("12. Top5 mes horas")
        print("13. Alterar registros")
        print("14. Simular")
        print("15. Salir")
        opcion = input("\nIngrese una opcion: ")
        
        if opcion == '1':
            top10_generos()
        elif opcion == '2':
            fecha1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            fecha2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            minutos_consum(fecha1, fecha2)
        elif opcion == '3':
            fecha1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            fecha2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            rep_categoria(fecha1, fecha2)
        elif opcion == '4':
            fecha1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            fecha2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            rep_cuenta(fecha1, fecha2)
        elif opcion == '5':
            cant_cuentas()
        elif opcion == '6':
            top10_actores()
        elif opcion == '7':
            top10_directores()
        elif opcion == '8':
            top10_busqueda()
        elif opcion == '9':
            fecha1 = input("Ingrese la fecha inicial (DD/MM/YYYY): ")
            fecha2 = input("Ingrese la fecha final (DD/MM/YYYY: ")
            top5_admins(fecha1,fecha2)
        elif opcion == '10':
            fecha1 = input("Ingrese la fecha inicial (DD/MM/YYYY: ")
            fecha2 = input("Ingrese la fecha final (DD/MM/YYYY: ")
            top20_noterminadas(fecha1,fecha2)
        elif opcion == '11':
            username = input("Ingrese el nombre de usuario: ")
            email = input("Ingrese el email: ")
            password = input("Ingrese la contraseña: ")
            name = input("Ingrese el nombre de la persona: ")
            Registro(username,email,password, name, 'Admin')

            connection = pass_manager.conexion()
            cursor = connection.cursor()
            codigo = """ SELECT CUsuario FROM usuario """
            cursor.execute(codigo)
            res = cursor.fetchall()[-1]

            Profiler('admin','99',res[0])
        elif opcion == '12':
            mes = input("Ingrese el mes (1-12): ")
            top5_mes_horas(mes)
        elif opcion == '13':
            alterar_registros()
        elif opcion == '14':
            simulacion.simulation_menu()
        elif opcion == '15':
            print("\nSaliendo...")

        else: print('Opcion invalida')




