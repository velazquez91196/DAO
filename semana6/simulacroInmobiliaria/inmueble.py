from abc import abstractmethod


class Inmueble:
    def __init__(self, tipo, codigo, nombre_propietario, alquiler_base, superficie):
        self._tipo = tipo
        self._codigo = codigo
        self._nombre_propietario = nombre_propietario
        self._alquiler_base = alquiler_base
        self._superficie = superficie

    @property
    @abstractmethod
    def calcular_importe_total(self):
        pass