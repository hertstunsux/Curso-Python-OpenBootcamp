def main():
    inputPaises = input('Introduzca una lista de países(separados por comas):')
    listaPaises = inputPaises.split(',')
    listaPaises = map(str.strip, listaPaises)
    seriePaises = set(listaPaises)
    paisesOrdenados = sorted(seriePaises)
    print(', '.join(paisesOrdenados))

if __name__=='__main__':
    main()
