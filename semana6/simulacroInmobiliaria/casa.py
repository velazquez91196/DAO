from inmueble import Inmueble


class Casa(Inmueble):
    def __init__(self, codigo, nombre_propietario, alquiler_base, superficie, cant_habitaciones, tiene_pileta):
        super().__init__(1, codigo, nombre_propietario, alquiler_base, superficie)
        self._cant_habitaciones = cant_habitaciones
        self._tiene_pileta = tiene_pileta

    @property
    def calcular_importe_total(self):
        alquiler_total = self._alquiler_base
        for i in range(self._cant_habitaciones):
            alquiler_total += 30000
        if self._tiene_pileta == 1:
            alquiler_total += 100000

        return alquiler_total

    def es_premium(self):
        return self._superficie > 150 and self._cant_habitaciones >= 2 and self._tiene_pileta == 1

    def __str__(self):
        return f'Casa {self._codigo} - {self._nombre_propietario} - {self._alquiler_base} - {self._superficie} - {self._cant_habitaciones} - {self._tiene_pileta}'