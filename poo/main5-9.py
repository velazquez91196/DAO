import csv
from persona import Persona


def leer_csv(archivo):
    datos = {}
    with open(archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            documento, nombre, apellido, edad = linea
            
            p = Persona(nombre, apellido, int(edad), documento)

            datos[documento] = p
    return datos


def cant_personas(v):
    return len(v.values())


def cant_mayores_edad(v):
    i = 0
    for persona in v.values():
        if persona.esMayorDeEdad():
            i += 1
    return i


def listado_apellido_vocal(v):
    lista = []
    for persona in v.values():
        if persona.apellidoVocal():
            lista.append((persona.nombre, persona.apellido))
    return lista

def cant_personas_x_apellido(v):
    cont = {}
    for persona in v.values():
        if persona.apellido in cont:
            cont[persona.apellido] += 1
        else:
            cont[persona.apellido] = 1
    return cont


def main():
    path = 'personas.csv'
    c_per = 0
    c_18 = 0
    lista_vocal = []
    c_ape = 0
    v = {}
    v = leer_csv(path)
    c_per = cant_personas(v)
    c_18 = cant_mayores_edad(v)
    lista_vocal = listado_apellido_vocal(v)
    c_ape = cant_personas_x_apellido(v)

    print(f'Cantidad de personas: {c_per}')
    print()
    print(f'Cantidad de personas mayores de edad: {c_18}')
    print()
    print(f'Listado de personas con apellido que comienza con vocal: {lista_vocal}')
    print()
    print(f'Cantidad de personas por apellido: {c_ape}')

if __name__ == '__main__':
    main()