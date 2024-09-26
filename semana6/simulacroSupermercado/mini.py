from abc import abstractmethod

from sucursal import Sucursal


class Mini(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, importe_alquiler):
        super().__init__(tipo, numero, superficie, facturacion)
        self.importe_alquiler = importe_alquiler

    @property
    def resultado_comercial(self):
        return self.facturacion - self.importe_alquiler

    @property
    def es_rentable(self):
        return self.indice_rentabilidad > 35

    @property
    def __str__(self):
        return f'{super().__str__} - {self.importe_alquiler}'