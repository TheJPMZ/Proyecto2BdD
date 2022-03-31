
from hash import hash
from operator import pos
import psycopg2




def conexion():
    connection = psycopg2.connect(user="postgres",
                                    password="clave",
                                    host="localhost",
                                    port="5432",
                                    database="Proyecto02")
    return connection


def check_user(user):
    try:
        connection = conexion()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT username FROM usuario WHERE username = '%s'"""
        cursor.execute(postgres_select_query % user)
        total = cursor.fetchall()
        if len(total)>0:    
            return True
        else: return False

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()


def check_pass(user,psswrd):
    try:
        connection = conexion()
        cursor = connection.cursor()
        if (check_user(user)):
            postgres_select_query = """ SELECT password FROM usuario WHERE username = '%s'"""
            cursor.execute(postgres_select_query % user)
            total = cursor.fetchall()
            password = total[0][0]
            if hash(psswrd) == password:
                return True
            else: return False
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")





print(check_pass('cayomol','mememememe'))
#print(check_pass(user,'fdjaodfjoad'))