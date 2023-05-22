import operaciones

def main():
    a = int (input("Ingrese primer número:"))
    b = int (input("Ingrese segundo número:"))
    print("La suma es {} \nLa resta es {} \nLa multiplicación es {} \nLa división (sin resto) es {} ".format(operaciones.suma(a,b),operaciones.resta(a,b),operaciones.multiplicacion(a,b),operaciones.division(a,b)))

if __name__ == '__main__':
    main()


