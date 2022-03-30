from tkinter       import Canvas, Frame, Tk
from Login         import gui as Login
from Signin        import gui as Sign
from SelectProfile import gui as SProfile
from CreateProfile import gui as CProfile



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


Login.run_window(window,canvas)



window.mainloop()



