#Menú de opciones al usuario
def mostrar_menu():
    print("\n-- Menu de Gestion de Pacientes --")
    print("1. Cargar pacientes")
    print("2. Mostrar todos los pacientes")
    print("3. Buscar paciente por Historia Clinica")
    print("4. Ordenar pacientes por Historia Clinica")
    print("5. Paciente con mas dias de internacion")
    print("6. Paciente con menos dias de internacion")
    print("7. Cantidad de pacientes con mas de 5 días de internacion")
    print("8. Promedio de días de internacion")
    print("9. Salir")
    return input("Seleccione una opción: ")



#Solicitar la cantidad de pacientes a ingresar y validar la entrada
def solicitar_cantidad_pacientes():
    while True:
        cantidad_input = input("¿Cuantos pacientes desea ingresar? ")
        if cantidad_input.isdigit():
            return int(cantidad_input)
        else:
            print("Entrada no valida. Por favor, ingrese un numero entero.")


#Solicitar el numero de historia clinica y validar la entrada
def solicitar_historia_clinica():
    while True:
        historia_input = input("Ingrese el numero de historia clinica: ")
        if historia_input.isdigit():
            return int(historia_input)
        else:
            print("Entrada no valida. Por favor, ingrese un numero entero.")


#Solicitar el nombre del paciente y validar la entrada
def solicitar_nombre():
    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        es_valido = True
        for caracter in nombre:
            if not (caracter.isalpha() or caracter.isspace()):
                es_valido = False
                break       
        if es_valido:
            return nombre
        else:
            print("Entrada no valida. Por favor, ingrese solo letras.")


#Solicitar la edad del paciente y validar la entrada
def solicitar_edad():
    while True:
        edad_input = input("Ingrese la edad del paciente: ")
        if edad_input.isdigit():
            edad = int(edad_input)
            return edad
        else:
            print("Entrada no valida. Por favor, ingrese numeros enteros.")


#Solicitar la cantidad de dias de internacion y validar la entrada
def solicitar_dias_internacion():
    while True:
        dias_input = input("Ingrese la cantidad de dias de internacion: ")
        if dias_input.isdigit():
            return int(dias_input)
        else:
            print("Entrada no valida. Por favor, ingrese un numero entero.")


#Carga la informacion de los pacientes
def cargar_pacientes(pacientes):
    cantidad_pacientes = solicitar_cantidad_pacientes()
    for _ in range(cantidad_pacientes):
        historia = solicitar_historia_clinica()
        nombre = solicitar_nombre()
        edad = solicitar_edad()
        diagnostico = input("Diagnostico: ")
        dias_internacion = solicitar_dias_internacion()
        pacientes.append([historia, nombre, edad, diagnostico, dias_internacion])
    print("Los pacientes se cargaron exitosamente.")


#Muestra la lista de pacientes registrados
def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            print(f"Historia Clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias de Internacion: {paciente[4]}")

#Buscar un paciente por su Historia Clinica
def buscar_paciente(pacientes):
    historia = int(input("Ingrese el numero de Historia Clinica a buscar: "))
    for paciente in pacientes:
        if paciente[0] == historia:
            print(f"Historia Clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias de Internacion: {paciente[4]}")
            return
    print("No se encontro el paciente.")

#Devuelve el número de historia clínica del paciente
def comparar_historia_clinica(paciente):
    return paciente[0]

#Ordena la lista de pacientes por numero de historia clínica
def ordenar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        pacientes.sort(key=comparar_historia_clinica)
        print("Pacientes ordenados por Historia Clinica.")


#Devuelve la cantidad de días de internación del paciente
def dias_internacion(paciente):
    return paciente[4]


#Determina el paciente con mas dias de internación
def paciente_mas_dias(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        max_dia_paciente = max(pacientes, key=dias_internacion)
        print(f"Paciente con más días de internación: Historia Clinica: {max_dia_paciente[0]}, Nombre: {max_dia_paciente[1]}, Días de Internación: {max_dia_paciente[4]}")

#Devuelve la cantidad de días de internación del paciente.
def dias_internacion(paciente):
    return paciente[4]


#Determina el paciente con menos dias de internacion
def paciente_menos_dias(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        min_dia_paciente = min(pacientes, key=dias_internacion)
        print(f"Paciente con menos días de internación: Historia Clínica: {min_dia_paciente[0]}, Nombre: {min_dia_paciente[1]}, Días de Internación: {min_dia_paciente[4]}")


#Cuenta la cantidad de pacientes con mas de 5 dias de internacion
def contar_pacientes_mas_5_dias(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        mas_de_cinco_dias= sum(1 for paciente in pacientes if paciente[4] > 5)
        print(f"Cantidad de pacientes con mas de 5 días de internacion: {mas_de_cinco_dias}")
        

#Calcula el promedio de los dias de internacion de todos los pacientes
def promedio_dias_internacion(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]    
    promedio = total_dias / len(pacientes)
    print(f"Promedio de dias de internacion: {promedio:.2f}")



#Funcion principal que ejecuta el programa
def main():
    pacientes = []
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            cargar_pacientes(pacientes)
        elif opcion == '2':
            mostrar_pacientes(pacientes)
        elif opcion == '3':
            buscar_paciente(pacientes)
        elif opcion == '4':
            ordenar_pacientes(pacientes)
        elif opcion == '5':
            paciente_mas_dias(pacientes)
        elif opcion == '6':
            paciente_menos_dias(pacientes)
        elif opcion == '7':
            contar_pacientes_mas_5_dias(pacientes)
        elif opcion == '8':
            promedio_dias_internacion(pacientes)
        elif opcion == '9':
            print("Finalizando sistema.")
            break
        else:
            print("Opcion no valida, por favor intente otra vez.")
