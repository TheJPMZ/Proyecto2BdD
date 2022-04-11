from tkinter       import Canvas, Tk
import login as Login
import createProfile as CProfile
import selectProfile as SProfile
import signIn as Sign







def createWindow():

    window = Tk()

    window.geometry("360x640")
    window.configure(bg = "#050840")

    canvas = Canvas(
        window,
        bg = "#050840",
        height = 640,
        width = 360,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    return window, canvas

def main():
    window, canvas = createWindow()
    Login.run_window(window, canvas)
    window.mainloop()



