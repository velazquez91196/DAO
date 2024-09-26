# moto.py
from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, matricula, modelo, costo_mantenimiento, cilindrada):
        super().__init__(3, marca, matricula, modelo, costo_mantenimiento)
        self.cilindrada = cilindrada

    @property
    def calcular_costo_mantenimiento(self):
        costo = self.costo_mantenimiento
        if self.cilindrada > 500:
            costo *= 1.20
        return costo

    def __str__(self):
        return f"Moto: {super().__str__()} - Cilindrada: {self.cilindrada} cc"