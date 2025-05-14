from cola_impresora import ColaImpresion
from menu import mostrar_menu

#Función principal del sistema de impresión
def ejecutar():
    impresora = ColaImpresion()  #Se crea la cola de impresión

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            #Entrada de datos del documento
            nombre = input("Escribe el nombre del documento: ").strip()
            usuario = input("¿Qué usuario envía el documento?: ").strip()
            try:
                paginas = int(input("Digite el número de páginas: "))
            except ValueError:
                print(" Número de páginas inválido.")
                continue
            impresora.agregar_documento(nombre, usuario, paginas)

        elif opcion == "2":
            impresora.procesar_documento()  #Procesa el documento actual

        elif opcion == "3":
            impresora.mostrar_cola()  #Muestra la cola de impresión

        elif opcion == "4":
            impresora.mostrar_actual()  #Muestra el documento en proceso

        elif opcion == "5":
            print(" Saliendo del sistema de impresión.")
            break

        else:
            print(" Opción inválida.")

#Inicia el programa si se ejecuta directamente
if __name__ == "__main__":
    ejecutar()
