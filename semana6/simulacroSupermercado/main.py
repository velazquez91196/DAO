from empresa import Empresa

def main():
    archivo = "sucursales.csv"
    empresa = Empresa()

    empresa.cargar_sucursales(archivo)

    print("Inmuebles cargados:")
    empresa.mostrar_sucursales()

    print("-" * 120)

    print("Suma de ganancias: ", empresa.sumar_ganancias())
    print("Cantidad de locales no rentables: ", empresa.cant_locales_no_rentables())
    print("Local más rentable: ", empresa.local_mas_rentable())

if __name__ == "__main__":
    main()