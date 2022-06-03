

import pass_manager
import hash
import psycopg2

import variables


def Registro(username,email,password, name, account):
    try:
        connection = pass_manager.conexion()
        cursor = connection.cursor()
        if pass_manager.check_user(username) == False:
            codigo = """ SELECT CUsuario FROM usuario """
            cursor.execute(codigo)
            res = cursor.fetchall()[-1]

            #Separar por numero
            res = res[0].split('U')[1]
            
            res = ''.join('U' + str(int(res)+1))

            password = hash.hash(password)

            postgres_select_query = """ INSERT INTO usuario(cusuario, username, nombre, password, email, cuenta, date) VALUES ('%s','%s','%s','%s','%s','%s',Now())"""
            cursor.execute(postgres_select_query % (res,username,name,password,email,account))
            
            
            connection.commit()

            variables.global_user = res
            variables.gloabl_acc = account
            return True
            
        else:
            return False
            
            
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


def Profiler(username, age, meme = None):
    try:

        if not meme:
            codig_usuario = variables.global_user
        else:
            codig_usuario = meme
        connection = pass_manager.conexion()
        cursor = connection.cursor()

        codigo = """ SELECT CPerfil FROM perfil"""
        cursor.execute(codigo)
        res = cursor.fetchall()[-1]

        newres = res[0][0:3] + str(int(res[0][3:])+1)

        postgres_select_query = """ INSERT INTO perfil(cperfil, cusuario, lognumber, profilename, edad) VALUES ('%s','%s','%s','%s','%s')"""
        cursor.execute(postgres_select_query % (newres, codig_usuario, 1, username, age))



        connection.commit()

        variables.global_profiles.append((variables.global_user, username, age, 1, variables.gloabl_acc, newres))

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)