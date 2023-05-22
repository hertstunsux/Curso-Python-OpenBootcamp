class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 150
    cilindrada = 200

coche = Coche()
print("Tengo un coche con velocidad de ", coche.velocidad, " Km, cilindrada de ", coche.cilindrada, " cc, de color ",coche.color, " con ", coche.puertas, " puertas y ", coche.ruedas, " ruedas ")
input("Presione cualquier tecla para salir")