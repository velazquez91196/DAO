from abc import abstractmethod, abstractproperty


class Sucursal:
    def __init__(self, tipo, numero, superficie, facturacion):
        self.tipo = tipo
        self.numero = numero
        self.superficie = superficie
        self.facturacion = facturacion

    @property
    @abstractmethod
    def resultado_comercial(self):
        pass

    @property
    @abstractmethod
    def es_rentable(self):
        pass

    @property
    def indice_rentabilidad(self):
        return self.resultado_comercial / self.superficie

    @property
    def __str__(self):
        return f'{self.tipo} - {self.numero} - {self.superficie} - {self.facturacion}'