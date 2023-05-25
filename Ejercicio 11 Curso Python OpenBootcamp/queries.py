import sqlite3
def main():
    insertar_usuarios()
    nombre = input("Ingrese el nombre del alumno a buscar:")
    print(busqueda_por_nombre(nombre))
def insertar_usuarios():
    id=int(input("Inserte el id del primer alumno:"))
    for i in range (id, id+8):
        nombre=input(f"Inserte el nombre del alumno {i}:")
        apellido=input(f"Inserte el apellido del alumno {i}:")
        crear_usuario(i, nombre, apellido)
def crear_usuario(id, nombre, apellido):
    conn= sqlite3.connect('Alumnos.db')
    cursor=conn.cursor()
    query = f"INSERT INTO Alumnos(id,nombre,apellido) VALUES ({id},'{nombre}','{apellido}')"
    rows = cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def busqueda_por_nombre(nombre):
    conn= sqlite3.connect('Alumnos.db')
    cursor=conn.cursor()

    query = f"SELECT * FROM Alumnos WHERE nombre = '{nombre}'"
    rows = cursor.execute(query)
    data = rows.fetchone()
    cursor.close()
    conn.close()
    if data is not None:
        return f"La persona {data[1]} {data[2]} es alumn@ con id {data[0]}"
    return "No se ha encontrado el alumno"

if __name__ == "__main__":
    main()