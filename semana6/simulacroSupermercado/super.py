from sucursal import Sucursal


class Super(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, es_mayorista):
        super().__init__(tipo, numero, superficie, facturacion)
        self.es_mayorista = es_mayorista

    @property
    def resultado_comercial(self):
        return self.facturacion

    @property
    def es_rentable(self):
        if self.es_mayorista == 1:
            return self.indice_rentabilidad > 45
        else:
            return self.indice_rentabilidad > 40

    @property
    def __str__(self):
        return f'{super().__str__} - {self.es_mayorista}'