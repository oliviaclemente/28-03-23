# Creamos una lista vacía para almacenar las personas
from ej1 import EstadoHospitalario, Persona


personas = []

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("1. Crear persona")
    print("2. Vacunar persona")
    print("3. Infectar persona")
    print("4. Mostrar información de una persona")
    print("5. Salir")

# Función para crear una nueva persona
def crear_persona():
    dni = input("Introduce el DNI de la persona: ")
    nombre = input("Introduce el nombre de la persona: ")
    edad = int(input("Introduce la edad de la persona: "))
    estado_hospitalario = input("Introduce el estado hospitalario de la persona (LEVE/MODERADO/SEVERO): ")
    estado_hospitalario = EstadoHospitalario[estado_hospitalario.upper()]  # Convertimos a enum
    persona = Persona(dni, nombre, estado_hospitalario, edad)
    personas.append(persona)
    print("Persona creada correctamente.")

# Función para vacunar a una persona
def vacunar_persona():
    dni = input("Introduce el DNI de la persona a vacunar: ")
    for persona in personas:
        if persona.dni == dni:
            if persona.vacunado() == 1:
                print("Persona vacunada correctamente.")
            else:
                print("No ha sido posible vacunar a la persona.")
            return
    print("No se ha encontrado ninguna persona con ese DNI.")

# Función para infectar a una persona
def infectar_persona():
    dni = input("Introduce el DNI de la persona a infectar: ")
    for persona in personas:
        if persona.dni == dni:
            impacto_covid = int(input("Introduce el impacto del COVID en la persona: "))
            nueva_carga_viral = persona.infectado(impacto_covid)
            if nueva_carga_viral == -1:
                print("La persona ha fallecido.")
            else:
                print("Nueva carga viral de la persona:", nueva_carga_viral)
            return
    print("No se ha encontrado ninguna persona con ese DNI.")

# Función para mostrar información de una persona
def mostrar_informacion_persona():
    dni = input("Introduce el DNI de la persona: ")
    for persona in personas:
        if persona.dni == dni:
            print(persona)
            return
    print("No se ha encontrado ninguna persona con ese DNI.")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    if opcion == "1":
        crear_persona()
    elif opcion == "2":
        vacunar_persona()
    elif opcion == "3":
        infectar_persona()
    elif opcion == "4":
        mostrar_informacion_persona()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
