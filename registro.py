import pass_manager
import hash
import psycopg2

def Registro(username,email,password, name, account):
    try:
        connection = pass_manager.conexion()
        cursor = connection.cursor()
        if pass_manager.check_user(username) == False:
            codigo = """ SELECT CODIGO FROM usuario ORDER BY CODIGO DESC LIMIT 1 """
            cursor.execute(codigo)
            res = cursor.fetchone()[0]
            
            #Separar por numero
            res = res.split('U')[1]
            
            res = ''.join('U' + str(int(res)+1))
            
            
            postgres_select_query = """ INSERT INTO usuario(edad,codigo,username,nombre,apellido,password, email) VALUES (20,'%s','%s','%s','','%s','%s')"""
            cursor.execute(postgres_select_query % (res,username,name,password,email))
            
            
            connection.commit()
            print('ejecutado')
            
        else:
            print('Nombre de usuario ya existe')
            
            
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        
        
Registro('Jorge01','juan@gmail.com','juan','juan','premium')