from abc import abstractmethod
from inmueble import Inmueble


class Departamento(Inmueble):
    def __init__(self, codigo, nombre_propietario, alquiler_base, superficie, expensas, piso):
        super().__init__(2, codigo, nombre_propietario, alquiler_base, superficie)
        self._expensas = expensas
        self._piso = piso

    @property
    def calcular_importe_total(self):
        alquiler_total = self._alquiler_base
        if self._piso < 3:
            alquiler_total += 20000
        alquiler_total += self._expensas

        return alquiler_total

    def __str__(self):
        return f'Departamento {self._codigo} - {self._nombre_propietario} - {self._alquiler_base} - {self._superficie} - {self._expensas} - {self._piso}'