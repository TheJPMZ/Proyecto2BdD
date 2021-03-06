
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, OptionMenu, messagebox
import login as Login
import createProfile as CProfile
import registro
import selectProfile as SProfile
import signIn as Sign
import webbrowser
import registro as reg
import variables

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")


lista = []

def move(destiny,window, canvas):
    for x in lista:
        x.destroy()
    destiny.run_window(window, canvas)

def some_callback(entry):
    entry.config(fg="black")# note that you must include the event as an arg, even if you don't use it.
    entry.delete(0, "end")
    return None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def run_window(window, canvas):

    canvas.delete("all")

    button_image_1 = PhotoImage(
        file=relative_to_assets("mini_return_button.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: move(Login,window, canvas),
        relief="flat"
    )
    button_1.place(
        x=40.0,
        y=558.0,
        width=135.0,
        height=55.0
    )
    lista.append(button_1)

    button_image_2 = PhotoImage(
        file=relative_to_assets("mini_signup_button.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Registrarse((entry_1,entry_2,entry_3,entry_5,cuenta)),
        relief="flat"
    )
    button_2.place(
        x=185.0,
        y=558.0,
        width=135.0,
        height=55.0
    )
    lista.append(button_2)
    

    image_image_1 = PhotoImage(
        file=relative_to_assets("text_area.png"))
    image_1 = canvas.create_image(
        180.0,
        285.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("text_entry.png"))
    entry_bg_1 = canvas.create_image(
        180.0,
        286.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0,
        fg = "grey"
    )
    entry_1.place(
        x=49.0,
        y=269.0,
        width=262.0,
        height=32.0
    )
    entry_1.insert(0, "Name")

    entry_1.bind("<Button-1>", lambda x: some_callback(entry_1))
    lista.append(entry_1)

    canvas.create_text(
        52.0,
        269.0,
        anchor="nw",
        text="Correo",
        fill="#414059",
        font=("Roboto", 24 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("text_area.png"))
    image_2 = canvas.create_image(
        180.0,
        210.0,
        image=image_image_2
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("text_entry.png"))
    entry_bg_2 = canvas.create_image(
        180.0,
        211.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0,
        fg = "grey"
    )
    entry_2.place(
        x=49.0,
        y=194.0,
        width=262.0,
        height=32.0
    )
    entry_2.insert(0, "Username")

    entry_2.bind("<Button-1>", lambda x: some_callback(entry_2))


    lista.append(entry_2)

    image_image_3 = PhotoImage(
        file=relative_to_assets("text_area.png"))
    image_3 = canvas.create_image(
        180.0,
        360.0,
        image=image_image_3
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("text_entry.png"))
    entry_bg_3 = canvas.create_image(
        180.0,
        361.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0,
        fg = "grey"
    )
    entry_3.place(
        x=49.0,
        y=344.0,
        width=262.0,
        height=32.0
    )
    entry_3.insert(0, "Password")

    entry_3.bind("<Button-1>", lambda x: some_callback(entry_3))

    lista.append(entry_3)

    image_image_4 = PhotoImage(
        file=relative_to_assets("mini_text_area.png"))
    image_4 = canvas.create_image(
        107.0,
        435.0,
        image=image_image_4
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("mini_text_entry.png"))
    entry_bg_4 = canvas.create_image(
        107.5,
        436.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0,
        fg="grey"
    )

    cuenta = StringVar(window)
    cuenta.set('Gratis [$0.00]')

    entry_4 = OptionMenu(window, cuenta, "Gratis [$0.00]", "Estandar [$5.50]", "Avanzada [$9.00]")

    entry_4.place(
        x=44.0,
        y=419.0,
        width=127.0,
        height=32.0
    )
    lista.append(entry_4)

    image_image_5 = PhotoImage(
        file=relative_to_assets("text_area.png"))
    image_5 = canvas.create_image(
        180.0,
        510.0,
        image=image_image_5
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("text_entry.png"))
    entry_bg_5 = canvas.create_image(
        180.0,
        511.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#F2F2F2",
        highlightthickness=0,
        fg = "grey"
    )
    entry_5.place(
        x=49.0,
        y=494.0,
        width=262.0,
        height=32.0
    )

    entry_5.insert(0, "Email")

    entry_5.bind("<Button-1>", lambda x: some_callback(entry_5))

    lista.append(entry_5)

    image_image_6 = PhotoImage(
        file=relative_to_assets("logo.png"))
    image_6 = canvas.create_image(
        180.0,
        84.0,
        image=image_image_6
    )

    canvas.create_text(
        52.0,
        494.0,
        anchor="nw",
        text="Password",
        fill="#414059",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        108.0,
        126.0,
        anchor="nw",
        text="SIGN UP",
        fill="#F2F2F2",
        font=("Roboto", 36 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("paypal_button.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: webbrowser.open_new("https://www.sandbox.paypal.com/checkoutnow?sessionID=uid_ba434f1f7d_mdm6ntu6mje&buttonSessionID=uid_17419790db_mdm6ntu6mje&stickinessID=uid_4687607bb9_mje6mtq6mdc&fundingSource=paypal&buyerCountry=GT&locale.x=es_ES&commit=true&clientID=AZDxjDScFpQtjWTOUtWKbyN_bDt4OgqaF4eYXlewfBP4-8aqX3PiV8e1GWU6liB2CUXlkA59kJXE7M6R&env=sandbox&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9c2IiLCJhdHRycyI6eyJkYXRhLWNzcC1ub25jZSI6IjVSZUNXUWg5V09kOVZXeWdpdHlOS3RpUEtCRUhoUXVnNlhoZW8reFUrQWpaZjU4YSIsImRhdGEtdWlkIjoidWlkX3pkampwem11bm5hYW9vcnZvc3Bmd29ta3lpa2tueiJ9fQ&xcomponent=1&version=5.0.289&token=2HD89204S12742922"),
        relief="flat"
    )
    button_3.place(
        x=185.0,
        y=408.0,
        width=135.0,
        height=55.0
    )
    lista.append(button_3)

    canvas.create_text(
        52.0,
        194.0,
        anchor="nw",
        text="Username",
        fill="#414059",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        52.0,
        344.0,
        anchor="nw",
        text="Full name",
        fill="#414059",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        49.0,
        419.0,
        anchor="nw",
        text="Advanced",
        fill="#050840",
        font=("Roboto", 24 * -1)
    )
    
    
    def Registrarse(entry):
        name = entry[0].get()
        username = entry[1].get()
        password = entry[2].get()
        email = entry[3].get()
        account = entry[4].get()[:-8]

        if not username.isalpha():
            messagebox.showwarning("alert", "Para su nombre de usuario no debe usar espacios ni caracteres no alfanumericos")
        elif not name.replace(" ","").isalpha():
            messagebox.showwarning("alert", "Lo que ha ingresado en su nombre no es valido")
        elif not email.replace("@","").replace(".","").isalpha():
            messagebox.showwarning("alert", "Lo que ha ingresado en su correo no es valido")
        else:

            if registro.Registro(username,email,password, name, account):
                variables.gloabl_acc = account
                move(SProfile, window, canvas)
            else:
                messagebox.showwarning("alert", "Usuario existente")

    window.resizable(False, False)
    window.mainloop()
