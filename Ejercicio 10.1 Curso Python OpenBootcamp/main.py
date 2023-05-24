import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tkinter.Tk()
selected_player = tkinter.StringVar(window,value="Ninguno")
def mostrarventana():
    showinfo(
        title='Jugador seleccionado',
        message=selected_player.get()
    )

def reset():
    selected_player.set(None)

jugadores = ["Messi","Cristiano","Maradona","Pele"]
for jugador in jugadores:
    radio_button = ttk.Radiobutton(window,text=jugador,variable=selected_player,value=f"Seleccionaste a {jugador}")
    radio_button.pack(ipadx=5,ipady=5)


boton_Seleccion = ttk.Button(window,text="Seleccione a su jugador",command=mostrarventana)
boton_Seleccion.pack(ipadx=5,ipady=5)

boton_Reinicio = ttk.Button(window,text="Resetear seleccion",command=reset)
boton_Reinicio.pack(ipadx=5,ipady=5)

if __name__ == '__main__':
    window.mainloop()


