import io

import psycopg2
from PIL import Image, ImageTk
from pathlib import Path
import time

# from tkinter import *
# Explicit imports to satisfy Flake8
from urllib.request import urlopen


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

def generateLista():
    try:
        connection = pass_manager.conexion()
        cursor = connection.cursor()

        codigo = """ SELECT * FROM pelicula WHERE clasificacion <= '%s'"""
        cursor.execute(codigo % variables.global_this_profile[2])
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


def run_window(window, canvas, profile):
    perfil = profile
    variables.global_this_profile = profile
    print(perfil)

    print(profile[5])



    canvas.delete("all")

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
        command=lambda: print("Search"),
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=82.0,
        width=33.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("star_button.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Favoritos"),
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
        def __init__(self,image,link,id):
            self.name = image

            self.button = Button(
                command=lambda: open_url(str(link),id),
                relief="flat",
                bg="#d80b1c",
                font=("Roboto", 28 * -1),
                fg="#f2f2f2",
                width=18,
                text=self.name.upper()
            )
            self.button.pack(pady=5)



            lista.append(self.button)

    def open_url(url,id):
        webbrowser.open(url)
        time.sleep(10)
        if variables.gloabl_acc == "Gratis":
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




    my_page = urlopen(
        'https://m.media-amazon.com/images/M/MV5BNjY0MGEzZmQtZWMxNi00MWVhLWI4NWEtYjQ0MDkyYTJhMDU0XkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_QL75_UX*_CR0,0,*_.jpg'
    )
    my_picture = io.BytesIO(my_page.read())
    pil_img = Image.open(my_picture)
    button_image_4 = ImageTk.PhotoImage(
        pil_img
    )
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_url(str(generateLista()[0][5])),
        relief="flat",
        width = 153.0,
        height = 229.0
    )
    button_4.place(
        x=185.0,
        y=130.0,
        width=153.0,
        height=229.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("clock_button.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Viendo"),
        relief="flat"
    )
    button_8.place(
        x=290.0000305175781,
        y=26.965850830078125,
        width=29.0,
        height=30.034149169921875
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("sugg_button.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Sugerencias"),
        relief="flat"
    )
    button_9.place(
        x=255.0,
        y=27.0,
        width=28.005111694335938,
        height=28.0738525390625
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
    lista.append(button_9)
    lista.append(entry_1)


    for x in generateLista():
        movieButton(x[1],x[5],x[0])

    window.resizable(False, False)
    window.mainloop()
