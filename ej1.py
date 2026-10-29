notas = {}
notas = {
"Salatic": [],
"Almada": [],
"Maldonado": [],
"Loberza": [],
"Perez": []
}
while True:
    print(" BIENVENIDO AL SISTEMA DE NOTAS ")
    print("1. ver todas las notas")
    print("2. ver notas por alumno")
    print("3. cargar notas")
    print("4. promedio")
    print("5. salir")
    opcion = int(input("Ingrese un aopcion: "))
    
    if opcion ==1:
        for apellidos in notas:
            print(f"Las notas de {apellido} son: {nota[apellidos]}")

    elif opcion ==2:
        apellido = str(input("Ingrese el apellido del alumno: ")).lower()
        if apellido in notas:
            print((f"Alumno: {apellido} y sus notas: {notas}"))
        else:
            print("El alumno no existe")

    elif opcion ==3:
        apellido = str(input("Ingrese el apellido del alumno: "))
        if apellido in notas:
            if len(notas[apellido]) == 0:
                for i in range(5):
                    nota = int(input(f"Ingrese la nota {i+1}"))
                    notas[apellidos].append(nota)
                    print(f"Las notas del alumno {apellido} fueron cargadas")
            else:
                print("Las notas del alumno ya estan cargadas")
        else:
            print("Ese alumno no existe")

    elif opcion ==4:
        str(input("Ingrese el apellido del alumno: ")).lower()
        if apellido in notas:
            if len(notas[apellidos]) == 5:
                suma = 0
                for notas in notas[apellido]:
                    suma = suma + notas
                    promedio = suma / 5
                    print(f"El promedio del alumno {apellido} es de: {promedio}")
            else:
                print("Todavia no se cargaron las 5 notas")
        else:
            print("Ese alumno no existe")

    elif opcion ==5:
        print("El programa finalizo")
        break
    
    else:
        print("Ingrese una opcion valida")
                        