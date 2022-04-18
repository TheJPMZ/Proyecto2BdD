import pass_manager
import hash
import psycopg2


def Profile(username, email, password, name, account):
    try:
        connection = pass_manager.conexion()
        cursor = connection.cursor()
        if pass_manager.check_user(username) == False:
            codigo = """ SELECT CUsuario FROM usuario ORDER BY CUsuario DESC LIMIT 1 """
            cursor.execute(codigo)
            res = cursor.fetchone()[0]

            # Separar por numero
            res = res.split('U')[1]

            res = ''.join('U' + str(int(res) + 1))

            postgres_select_query = """ INSERT INTO usuario(cusuario, username, nombre, password, email, cuenta) VALUES ('%s','%s','%s','%s','%s','%s')"""
            cursor.execute(postgres_select_query % (res, username, name, password, email, account))

            connection.commit()
            return True

        else:
            return False


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)