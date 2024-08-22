# Definir funciones para operaciones aritméticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

# Función principal
def calculadora():
    while True:
        mostrar_menu()
        op = input("Ingrese su opción (1/2/3/4/5): ")

        if op == '5':
            print("Saliendo...")
            break

        if op in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Entrada inválida. Por favor ingrese números válidos.")
                continue

            if op == '1':
                print(f"Resultado: {suma(num1, num2)}")
            elif op == '2':
                print(f"Resultado: {resta(num1, num2)}")
            elif op == '3':
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif op == '4':
                print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    calculadora()