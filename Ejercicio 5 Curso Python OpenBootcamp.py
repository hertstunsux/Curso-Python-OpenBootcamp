esbisiesto = lambda año: True if año%4==0 else False
año = int(input("Introduzca el año:"))
if esbisiesto(año):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
input("Presione cualquier tecla para salir")