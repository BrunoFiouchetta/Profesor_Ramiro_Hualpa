while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre.isalpha():
        break 
    else:
        print("Nombre invalido, intente nuevamente (solo letras).")

while True:
    apellido = input("Ingresa tu apellido: ")
    if apellido.isalpha():
        break 
    else:
        print("Apellido invalido, intente nuevamente (solo letras).")

nombre_completo = nombre + " " + apellido

def validar_dni(dni: str) -> bool:
    dni_limpio = dni.replace(".", "")
    
    if len(dni_limpio) == 8 and dni_limpio.isdigit():
        return True
    return False

while True:
    dni = input("Ingresa tu DNI (con o sin puntos): ")
    if validar_dni(dni):
        break
    else:
        print("DNI invalido, intente nuevamente.")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

while True:
    try:
        obra_social = input("¿Tenes obra social? (Si o No): ")
        if(obra_social.lower() == "si" or obra_social.lower() == "no"):
            break
    except ValueError:
        print("Por favor, ingresa Si o No.")

while True:
    try:
        prioridad = input("Ingresa la prioridad de tu turno (1 = emergencia, 2 = urgente, 3 = control): ")
        if prioridad in ["1", "2", "3"]:
            if prioridad == "1":
                print("Turno asignado inmediatamente a guardia")
            if prioridad == "2":
                if obra_social.lower() == "si":
                    print("Turno asignado en menos de 24 horas")
                else:
                    print("Turno asignado en 48 horas")
            if prioridad == "3":
                if edad > 65:
                    print("Turno preferencial en 72 horas")
                else:
                    print("Turno asignado en 7 dias")
            break
    except ValueError:
        print("Por favor, ingresa una prioridad valida.")