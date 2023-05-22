from functools import reduce
def main():
    total = int(input('Introduzca la cantidad de elementos de la lista:'))
    lista = []
    for i in range(0,total):
        lista.append(int(input(f'Introduzca el elemento {i+1} a la lista:')))
    Suma = reduce(lambda sumando1, sumando2: sumando1 + sumando2, filter(lambda impar: impar % 2 == 1,lista))
    print(f'La suma de impares de su lista es {Suma}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
