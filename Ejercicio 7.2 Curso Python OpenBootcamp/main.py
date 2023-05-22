import time
def main():
    entrada = int(input("Ingrese su hora de entrada al trabajo(ej. 8, 9):"))
    hora = time.localtime().tm_hour
    minutos = time.localtime().tm_min
    segundos =time.localtime().tm_sec
    if(hora>19):
        print("Es hora de salir")
    elif(hora<entrada):
        print("Todavía no entras a trabajar")
    else:
        totalTiempoFaltante= 19*3600 - hora*3600 - minutos*60 - segundos
        horasFaltantes = totalTiempoFaltante//3600
        minutosFaltantes = totalTiempoFaltante//60 - horasFaltantes*60
        segundosFaltantes = totalTiempoFaltante - horasFaltantes*3600 - minutosFaltantes*60
        print("Faltan {} horas, {} minutos, y {} segundos para salir".format(horasFaltantes,minutosFaltantes,segundosFaltantes))


if __name__ == '__main__':
    main()

