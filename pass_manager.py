from datetime import datetime
from tkinter import messagebox
import time

from hash import hash
from operator import pos
import psycopg2

def conexion():
    connection = psycopg2.connect(user="postgres",
                                    password="iamgreat",
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
        print("Failed to connect to the database", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()


def check_pass(user,pss):
    psswrd = hash(pss)
    try:
        connection = conexion()
        cursor = connection.cursor()
        if (check_user(user)):

            postgres_select_query = """ SELECT * FROM loginLog order by codigo desc"""
            cursor.execute(postgres_select_query)
            res = cursor.fetchone()[0]
            code = str(int(res)+1)

            ts = time.time()

            postgres_select_query = """ INSERT INTO loginlog(codigo, uingreso, pingreso, fecha) VALUES ('%s','%s','%s','%s')"""
            cursor.execute(postgres_select_query % (code,user,psswrd,ts))
            connection.commit()

            postgres_select_query = """ SELECT password FROM usuario WHERE username = '%s'"""
            cursor.execute(postgres_select_query % user)
            total = cursor.fetchall()
            password = total[0][0]
            if psswrd == password:
                return True
            else: return False
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")
        print("Failed to connect to the database", error)






#print(check_pass(user,'fdjaodfjoad'))