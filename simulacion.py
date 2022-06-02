import psycopg2
import random
import datetime
from pass_manager import conexion


def executequery(p_cursor, p_query, parameters=None):
    try:
        if parameters:
            p_cursor.execute(p_query % parameters)
        else:
            p_cursor.execute(p_query)
    except psycopg2.Error as e:
        print("Ocurrio un error: ", e)
        exit()
    return p_cursor


def simulate(p_querystring):
    connection = conexion()
    cursor = connection.cursor()

    query1 = """SELECT cperfil FROM Perfil"""

    executequery(cursor, query1)
    result = cursor.fetchall()

    profile = random.choice(result)

    query2 = """SELECT cpelicula FROM Pelicula"""

    executequery(cursor, query2)
    result = cursor.fetchall()

    movie = random.choice(result)

    query3 = """SELECT duracion FROM Pelicula WHERE cpelicula = '%s'"""

    executequery(cursor, query3, movie[0])
    result = cursor.fetchall()

    duration = result[0]

    if random.randint(0, 1):
        duration = int(duration[0])
    else:
        duration = random.randint(0, *duration)

    insert_query = """INSERT INTO ver (cperfil, cpelicula, duracion, fecha, timestmp) VALUES ('%s','%s','%s',%s,%s)"""

    executequery(cursor, insert_query, (*profile, *movie, duration, p_querystring, p_querystring))

    connection.commit()
    cursor.close()
    connection.close()


def simulation_menu():
    year, month, day = str(datetime.date.today()).split("-")

    class DayError:
        pass

    try:
        new_year = int(input("Enter the year: "))
        new_month = int(input("Enter the number of the month: "))
        new_day = int(input("Enter the number of the day: "))

        1 / new_year * new_month * new_day

        if new_year <= 0 or new_month <= 0 or new_day <= 0:
            raise ZeroDivisionError

        if new_month > 12:
            raise StopIteration

        if new_day > 31:
            raise DayError
        elif new_month == 2 and new_day > 28:
            raise DayError
        elif new_month in [4, 6, 9, 11] and new_day > 31:
            raise DayError

    except ValueError:
        print("Ingresar solamente numeros enteros")
    except ZeroDivisionError:
        print("No se permiten numeros menores o iguales a 0")
    except StopIteration:
        print("Los meses deben ser menores a 12")
    except DayError:
        print("Hubo un error en el dia")
    else:

        try:
            repeats = int(input("Numero de datos a generar: "))

            for x in range(0, repeats):
                year_interval = new_year - int(year)
                month_interval = new_month - int(month)
                day_interval = new_day - int(day)
                hour_interval = random.randint(-20, 2)
                minute_interval = random.randint(0, 59)
                seconds_interval = random.randint(0, 59)

                querystring = f"NOW() + INTERVAL '{year_interval} years {month_interval} months {day_interval} days {hour_interval} hours {minute_interval} minutes {seconds_interval} seconds' "

                print(x * 100 / repeats, "%", end="\r")

                simulate(querystring)

            print("Done!!")
        except Exception:
            print("Ese no es un numero valido")


def simulate2():
    for daya in range(0, 60):
        for x in range(0, 750):
            year_interval = 0
            month_interval = 0
            day_interval = daya
            hour_interval = random.randint(-20, 2)
            minute_interval = random.randint(0, 59)
            seconds_interval = random.randint(0, 59)

            querystring = f"NOW() + INTERVAL '{year_interval} years {month_interval} months {day_interval} days {hour_interval} hours {minute_interval} minutes {seconds_interval} seconds'"

            print((((x * 100) / 750) * daya) / 60, "%", end="\r")

            simulate(querystring)

    print("Done!!")
