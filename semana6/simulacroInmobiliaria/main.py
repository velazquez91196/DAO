import csv
import functools

from inmobiliaria import Inmobiliaria

def main():
    archivo = "inmuebles.csv"
    inmobiliaria = Inmobiliaria()

    inmobiliaria.cargar_inmuebles(archivo)

    print("Inmuebles cargados:")
    inmobiliaria.mostrar_inmuebles()

    print("-" * 120)
    print("Suma de alquileres:", inmobiliaria.sumar_alquileres())
    print("Cantidad de casas premium:", inmobiliaria.cantidad_casas_premium())
    print("Propietario con alquiler más bajo: ", inmobiliaria.propietario_con_alquiler_mas_bajo())


if __name__ == "__main__":
    main()