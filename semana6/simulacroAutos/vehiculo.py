from abc import abstractproperty, abstractmethod


class Vehiculo:
    def __init__(self, tipo, marca, matricula, modelo, costo_mantenimiento):
        self.tipo = tipo
        self.marca = marca
        self.matricula = matricula
        self.modelo = modelo
        self.costo_mantenimiento = costo_mantenimiento


    def __str__(self):
        return f"{self.tipo} {self.marca} {self.matricula} {self.modelo} "

    @property
    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass