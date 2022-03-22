
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from SelectProfile import gui as SProfile

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

lista = []

def move(destiny,window, canvas):
    for x in lista:
        x.destroy()
    destiny.run_window(window, canvas)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def run_window(window,canvas):

    canvas.delete("all")

    canvas.create_text(
        40.0,
        34.0,
        anchor="nw",
        text="CREATE PROFILE",
        fill="#F2F2F2",
        font=("Roboto", 36 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: move(SProfile, window, canvas),
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=534.0,
        width=280.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=40.0,
        y=460.0,
        width=280.0,
        height=55.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        180.0,
        329.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        180.0,
        330.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0
    )
    entry_1.place(
        x=49.0,
        y=313.0,
        width=262.0,
        height=32.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        180.0,
        408.0,
        image=image_image_2
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        180.0,
        409.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0
    )
    entry_2.place(
        x=49.0,
        y=392.0,
        width=262.0,
        height=32.0
    )

    canvas.create_text(
        56.0,
        313.0,
        anchor="nw",
        text="Username",
        fill="#414059",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        56.0,
        392.0,
        anchor="nw",
        text="Age",
        fill="#414059",
        font=("Roboto", 24 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        179.0,
        194.0,
        image=image_image_3
    )
    window.resizable(False, False)

    lista.append(button_1)
    lista.append(button_2)
    lista.append(entry_1)
    lista.append(entry_2)

    window.mainloop()

