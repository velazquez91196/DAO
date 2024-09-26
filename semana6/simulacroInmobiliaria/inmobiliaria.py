import csv
from functools import reduce

from casa import Casa
from departamento import Departamento

class Inmobiliaria:
    def __init__(self):
        self._inmuebles = []

    def cargar_inmuebles(self, archivo):
        with open(archivo, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tipo = int(row[0])
                codigo = str(row[1])
                nombre_propietario = str(row[2])
                alquiler_base = float(row[3])
                superficie = float(row[4])
                if tipo == 1:
                    cant_habitaciones = int(row[5])
                    tiene_pileta = int(row[6])
                    inmueble = Casa(codigo, nombre_propietario, alquiler_base, superficie, cant_habitaciones, tiene_pileta)
                elif tipo == 2:
                    expensas = float(row[5])
                    piso = int(row[6])
                    inmueble = Departamento(codigo, nombre_propietario, alquiler_base, superficie, expensas, piso)
                self._inmuebles.append(inmueble)
        return self._inmuebles

    def mostrar_inmuebles(self):
        for inmueble in self._inmuebles:
            print(inmueble.__str__())

    def sumar_alquileres(self):
        return sum(inmueble.calcular_importe_total for inmueble in self._inmuebles)

    def cantidad_casas_premium(self):
        return sum(1 for inmueble in self._inmuebles if inmueble._tipo == 1 and inmueble.es_premium())

    def propietario_con_alquiler_mas_bajo(self):
        return reduce(lambda x, y: x if x.calcular_importe_total < y.calcular_importe_total else y, self._inmuebles)._nombre_propietario
