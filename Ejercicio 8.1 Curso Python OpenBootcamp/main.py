
def main():
    for iteracion in range (2):
        fichero = open('texto.txt', 'a')
        texto = input(f'Ingrese el texto número {iteracion +1}:')
        if not texto.endswith('\n'):
            texto+='\n'
        fichero.write(texto)
        fichero.close()

if __name__ == '__main__':
    main()

