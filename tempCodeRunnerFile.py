# Definimos una función para cada operación

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero."

# Función para mostrar el menú y obtener la opción del usuario

def mostrar_menu():
    print("\nCalculadora básica")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    return input("Seleccione la operación (1/2/3/4/5): ")

# Función principal para ejecutar el programa

def main():
    while True:
        opcion = mostrar_menu()

        # Opción para salir del programa
        
        if opcion == '5':
            print("Saliendo del programa. ¡Adiós!")
            break
        
  # Solicitamos los números al usuario si la opción no es salir
  
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
    # Realizamos la operación según la opción seleccionada
    
    if opcion == '1':
        resultado = sumar(num1, num2)
        signo = '+'
    elif opcion == '2':
        resultado = restar(num1, num2)
        signo = '-'
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        signo = '*'
    elif opcion == '4':
        resultado = dividir(num1, num2)
        signo = '/'
    else:
        print("Opción inválida")
        return

    # Mostramos el resultado
    
    print(f"Resultado: {num1} {signo} {num2} = {resultado}")

# Ejecutamos el programa principal

if __name__ == "__main__":
    main()