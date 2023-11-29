from tkinter import *
from frame import *


def main():
    ventana = tk.Tk()
    ventana.wm_title("                            PROYECTO INTEGRADOR 2023                     ")
    ventana.geometry("800x600")
    ventana.tk.call('wm', 'iconphoto', ventana._w, PhotoImage(file="logo.png"))

    app = VENTANA(ventana)

    app.mainloop()


if __name__ == ("__main__"):
    main()