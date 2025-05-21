from conversion import infija_a_postfija
from evaluacion import evaluar_postfija

# Muestra las opciones disponibles al usuario
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Convertir expresión infija a postfija")
    print("2. Evaluar expresión postfija")
    print("3. Salir")

# Ejecuta la opción seleccionada por el usuario
def ejecutar_opcion(opcion):
    if opcion == '1':
        expr = input("Ingrese la expresión infija: ")
        postfija = infija_a_postfija(expr)
        print("Expresión postfija:", postfija)
    elif opcion == '2':
        expr = input("Ingrese la expresión postfija (solo dígitos y operadores): ")
        resultado = evaluar_postfija(expr)
        print("Resultado:", resultado)
    elif opcion == '3':
        print("Saliendo del programa...")
    else:
        print("Opción inválida.")