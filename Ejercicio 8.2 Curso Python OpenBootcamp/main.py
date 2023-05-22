import pickle
class Vehiculo:
    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas
    def __str__(self):
        return f'Este es un auto de color {self.color} con {self.puertas} puertas y {self.ruedas} ruedas'

def main():
    """
    Solo utilizo este código la primera vez para crear el archivo binario:

    V1 = Vehiculo("Rojo", 4, 4)
    fichero = open('Vehiculo.bin','wb')
    pickle.dump(V1,fichero)
    fichero.close()
    """
    
    fichero2 = open('Vehiculo.bin','rb')
    V2 = pickle.load(fichero2)
    print(V2)

if __name__ == '__main__':
    main()

