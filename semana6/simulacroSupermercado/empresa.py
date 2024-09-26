from mini import Mini
from super import Super
from hiper import Hiper
import csv
import functools

class Empresa:
    def __init__(self):
        self.sucursales = []

    def cargar_sucursales(self, archivo):
        with open(archivo, newline='') as file:
            reader = csv.reader(file)
            for linea in reader:
                tipo = int(linea[0])
                numero = int(linea[1])
                superficie = float(linea[2])
                facturacion = float(linea[3])
                if tipo == 1:
                    ganancia_alquileres = float(linea[4])
                    sucursal = Hiper(tipo, numero, superficie, facturacion, ganancia_alquileres)
                elif tipo == 2:
                    es_mayorista = int(linea[4])
                    sucursal = Super(tipo, numero, superficie, facturacion, es_mayorista)
                elif tipo == 3:
                    importe_alquiler = float(linea[4])
                    sucursal = Mini(tipo, numero, superficie, facturacion, importe_alquiler)
                self.sucursales.append(sucursal)
        return self.sucursales

    def mostrar_sucursales(self):
        for sucursal in self.sucursales:
            print(sucursal.__str__)

    def sumar_ganancias(self):
        return sum(sucursal.resultado_comercial for sucursal in self.sucursales)

    def cant_locales_no_rentables(self):
        return sum(1 for sucursal in self.sucursales if not sucursal.es_rentable)

    def local_mas_rentable(self):
        rentable = functools.reduce(lambda x, y: x if x.indice_rentabilidad > y.indice_rentabilidad else y, self.sucursales)
        return f'Número de sucursal {rentable.numero} - Tipo: {rentable.tipo}'