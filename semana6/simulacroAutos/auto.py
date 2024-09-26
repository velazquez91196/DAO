from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, matricula, modelo, costo_mantenimiento, kilometraje):
        super().__init__(1, marca, matricula, modelo, costo_mantenimiento)
        self.kilometraje = kilometraje

    @property
    def calcular_costo_mantenimiento(self):
        costo = self.costo_mantenimiento
        if self.kilometraje > 100000:
            costo *= 1.10
        return costo

    def __str__(self):
        return f"Auto: {super().__str__()} - Kilometraje: {self.kilometraje}"