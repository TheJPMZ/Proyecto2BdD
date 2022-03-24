

from operator import pos
import psycopg2





def check_user(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="psswrd",
                                    host="localhost",
                                    port="5432",
                                    database="Proyecto02")
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
            print("PostgreSQL connection is closed")


def check_pass(psswrd):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="psswrd",
                                    host="localhost",
                                    port="5432",
                                    database="Proyecto02")
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM usuario WHERE password = '%s'"""
        cursor.execute(postgres_select_query % psswrd)
        total = cursor.fetchall()
        print(total)
        if len(total)>0:    
            return True
        else: 
            return False
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



user = "jmpz"


print(check_pass("pepepepepep"))