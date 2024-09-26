from abc import abstractmethod

from sucursal import Sucursal


class Hiper(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, ganancia_alquileres):
        super().__init__(tipo, numero, superficie, facturacion)
        self.ganancia_alquileres = ganancia_alquileres

    @property
    def resultado_comercial(self):
        return self.facturacion + self.ganancia_alquileres

    @property
    def es_rentable(self):
        return self.indice_rentabilidad > 50

    @property
    def __str__(self):
        return f'{super().__str__} - {self.ganancia_alquileres}'