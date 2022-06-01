import io

import psycopg2
from PIL import Image, ImageTk
from pathlib import Path
import time

# from tkinter import *
# Explicit imports to satisfy Flake8
from urllib.request import urlopen

import busqueda
import login as Login
import createProfile as CProfile
import pass_manager
import selectProfile as SProfile
import signIn as Sign
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import webbrowser

import variables

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generateLista(querie,parametro):
    try:
        connection = pass_manager.conexion()
        cursor = connection.cursor()

        codigo = querie
        cursor.execute(codigo % parametro)
        peliculas = cursor.fetchall()

        print(peliculas)
        connection.commit()

        return peliculas

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)


lista = []


def move(destiny, window, canvas):
    for x in lista:
        x.destroy()
    destiny.run_window(window, canvas)

def reload(window, canvas, listapeliculas):
    for x in lista:
        x.destroy()
    run_window(window, canvas, variables.global_this_profile, listapeliculas, variables.global_this_profile[5])


def run_window(window, canvas, profile, querie = """ SELECT * FROM pelicula WHERE clasificacion <= '%s'""",parametro=""):
    perfil = profile
    variables.global_this_profile = profile

    print("Parametro: " + parametro)
    if parametro == "":
        parametro = variables.global_this_profile[2]


    canvas.delete("all")

    def clear():
        list = window.grid_slaves()
        for l in list:
            l.destroy()
    clear()

    canvas = Canvas(
        window,
        bg="#050840",
        height=640,
        width=360,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        360.0,
        18.0,
        fill="#BF0A19",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("search_button.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: search(entry_1.get()),
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=82.0,
        width=33.0,
        height=31.0
    )

    def search(string):
        busqueda.display_cualquiera(string)

    button_image_2 = PhotoImage(
        file=relative_to_assets("star_button.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: reload(window, canvas,"""SELECT cpelicula, nombre, duracion, clasificacion, imagen, link, director
FROM favoritos
NATURAL JOIN perfil
NATURAL JOIN pelicula
WHERE cperfil = '%s'"""),
        relief="flat"
    )
    button_2.place(
        x=323.0,
        y=26.0,
        width=30.0,
        height=31.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("back_button.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    button_3.place(
        x=8.0,
        y=25.0,
        width=24.0,
        height=30.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("search_entry.png"))
    entry_bg_1 = canvas.create_image(
        201.0,
        97.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0
    )
    entry_1.place(
        x=87.0,
        y=86.0,
        width=228.0,
        height=20.0
    )



    "===========MOVIE BUTTONS================="
    class movieButton:
        def __init__(self,image,link,id,coords):
            self.name = image

            self.button = Button(
                command=lambda: open_url(str(link),id),
                relief="flat",
                bg="#d80b1c",
                font=("Roboto", 20 * -1),
                fg="#f2f2f2",
                width= 20,
                text=self.name.upper()
            )
            self.button.place(
                x = 65,
                y = coords
            )



            lista.append(self.button)

    def open_url(url,id):
        try:
            connection = pass_manager.conexion()
            cursor = connection.cursor()

            postgres_select_query = """ INSERT INTO ver(cperfil, cpelicula, duracion, fecha, timestmp) VALUES ('%s','%s','%s',Now(),Now())"""
            cursor.execute(postgres_select_query % (variables.global_this_profile[5], id, 0.5))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error al ingresar datos a la tabla ver", error)

        webbrowser.open(url)
        time.sleep(10)

        if variables.global_this_profile[4] == "Gratis":
            try:
                connection = pass_manager.conexion()
                cursor = connection.cursor()
                codigo = """ SELECT anuncio
                            from pelicula
                            NATURAL JOIN adbreak
                            NATURAL JOIN anuncios
                            WHERE cpelicula = '%s'"""
                cursor.execute(codigo % id)
                res = cursor.fetchone()[0]


                connection.commit()


                webbrowser.open(str(res))
            except (Exception, psycopg2.Error) as error:
                print("Error while fetching data from PostgreSQL", error)


    button_image_8 = PhotoImage(
        file=relative_to_assets("clock_button.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: reload(window, canvas, """SELECT ver.cpelicula, nombre, pelicula.duracion, clasificacion, imagen, link, director
FROM ver
NATURAL JOIN perfil
JOIN pelicula on pelicula.cpelicula = ver.cpelicula
WHERE cperfil = '%s'"""),
        relief="flat"
    )
    button_8.place(
        x=290.0000305175781,
        y=26.965850830078125,
        width=29.0,
        height=30.034149169921875
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("logo.png"))
    image_1 = canvas.create_image(
        177.0,
        51.0,
        image=image_image_1
    )

    lista.append(button_1)
    lista.append(button_2)
    lista.append(button_3)
    lista.append(button_8)
    lista.append(entry_1)

    coordenadas = 150


    for x,y in enumerate(generateLista(querie,parametro)):
        movieButton(y[1],y[5],y[0],coordenadas)
        coordenadas += 50

    window.resizable(False, False)
    window.mainloop()
