# camioneta.py
from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, marca, matricula, modelo, costo_mantenimiento, capacidad_carga):
        super().__init__(2, marca, matricula, modelo, costo_mantenimiento)
        self.capacidad_carga = capacidad_carga

    @property
    def calcular_costo_mantenimiento(self):
        costo = self.costo_mantenimiento
        if self.capacidad_carga > 1000:
            costo *= 1.15
        return costo

    def __str__(self):
        return f"Camioneta: {super().__str__()} - Capacidad de Carga: {self.capacidad_carga} kg"