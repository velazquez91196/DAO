import random


'''
def borde_x(x):
    if x < 0:
        x = 0
    elif x > 400:
        x = 400
    return x

def borde_y(y):
    if y < 0:
        y = 0
    elif y > 400:
        y = 400
    return y

def revisar_posicion(x, y):
    if x < 0 or x > 400 or y < 0 or y > 400:
        print("El robot se saldrá de la cuadrícula... Estableciendo posición en borde...")
        x = borde_x(x)
        y = borde_y(y)
    return x, y
'''

borde_x = lambda x: 0 if x < 0 else 400

revisar_posicion_x = lambda x: x if 0 < x < 400 else borde_x(x)

borde_y = lambda y: 0 if y < 0 else 400

revisar_posicion_y = lambda y: y if 0 < y < 400 else borde_y(y)


# Funciones de movimiento
'''def mov_norte(x, y):
    y = y + 10
    x, y = revisar_posicion(x, y)
    return x, y
'''

mov_norte = lambda x, y: (revisar_posicion_x(x), revisar_posicion_y(y + 10))

mov_sur = lambda x, y: (revisar_posicion_x(x), revisar_posicion_y(y - 20))

mov_este = lambda x, y: (revisar_posicion_x(x + 10), revisar_posicion_y(y))

mov_oeste = lambda x, y: (revisar_posicion_x(x - 20), revisar_posicion_y(y))


'''
def mov_sur(x, y):
    y = y - 20
    x, y = revisar_posicion(x, y)
    return x, y

def mov_este(x, y):
    x = x + 10
    x, y = revisar_posicion(x, y)
    return x, y

def mov_oeste(x, y):    
    x = x - 20
    x, y = revisar_posicion(x, y)
    return x, y

'''

def mostrar_menu():
    print("Seleccione una tipo de movimiento: ")
    print("N. girar al norte y avanzar 10 pasos")
    print("S. Girar al sur y avanzar 20 pasos")
    print("E. Girar al este y avanzar 10 pasos")
    print("O. Girar al oeste y avanzar 20 pasos")
    print("F. Finalizar")

# Función principal
def tito():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    
    pos = (x, y)
    
    print(f"La posición inicial es: {pos}")

    while True:
        mostrar_menu()
        
        op = input("Ingrese su opción (N/S/E/O/F): ")

        if op == 'F':
            print("Saliendo...")
            break

        if op in ['N', 'S', 'E', 'O']:
            if op == 'N':
                x, y = mov_norte(x, y)
            elif op == 'S':
                x, y = mov_sur(x, y)
            elif op == 'E':
                x, y = mov_este(x, y)
            elif op == 'O':
                x, y = mov_oeste(x, y)
            print(f"Nueva posición: {x, y}")
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    tito()