import tkinter

def seleccionar(equipo):
    seleccion.config(text=f"Ha seleccionado el {equipo}")

window = tkinter.Tk()
equipo_seleccionado= tkinter.StringVar(window)
lista_equipos= tkinter.OptionMenu(window,equipo_seleccionado,"Arsenal", "Liverpool", "Manchester City", "Tottenham Hotspur",command=seleccionar)
lista_equipos.pack()
seleccion = tkinter.Label(window,text="Ningún equipo seleccionado")
seleccion.pack()


if __name__ == '__main__':
    window.mainloop()

