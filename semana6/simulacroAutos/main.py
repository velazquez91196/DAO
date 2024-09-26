import csv
import functools

from auto import Auto
from camioneta import Camioneta
from moto import Moto


def cargar_vehiculos(archivo):
    vehiculos = []
    with open(archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tipo = int(row[0])
            marca = str(row[1])
            matricula = str(row[2])
            modelo = str(row[3])
            costo_mantenimiento = float(row[4])
            if tipo == 1:
                kilometraje = float(row[5])
                vehiculo = Auto(marca, matricula, modelo, costo_mantenimiento, kilometraje)
            elif tipo == 2:
                capacidad_carga = float(row[5])
                vehiculo = Camioneta(marca, matricula, modelo, costo_mantenimiento, capacidad_carga)
            elif tipo == 3:
                cilindrada = float(row[5])
                vehiculo = Moto(marca, matricula, modelo, costo_mantenimiento, cilindrada)
            vehiculos.append(vehiculo)
    return vehiculos


def calcular_costo_total_mantenimiento(vehiculos):
    return sum(vehiculo.calcular_costo_mantenimiento for vehiculo in vehiculos)

def obtener_vehiculo_costo_mas_alto(vehiculos):
    return functools.reduce(lambda x, y: x if x.calcular_costo_mantenimiento > y.calcular_costo_mantenimiento else y, vehiculos)


def contar_camionetas_mas_1000kg(vehiculos):
    return sum(1 for vehiculo in vehiculos if isinstance(vehiculo, Camioneta) and vehiculo.capacidad_carga > 1000)


def contar_motos_alta_cilindrada(vehiculos):
    return sum(1 for vehiculo in vehiculos if isinstance(vehiculo, Moto) and vehiculo.cilindrada > 500)


if __name__ == "__main__":
    archivo = 'vehiculos.csv'
    vehiculos = cargar_vehiculos(archivo)

    costo_total = calcular_costo_total_mantenimiento(vehiculos)
    print(f"Costo total de mantenimiento: {costo_total}")

    vehiculo_mas_caro = obtener_vehiculo_costo_mas_alto(vehiculos)
    print(f"Vehículo con el costo de mantenimiento más alto: {vehiculo_mas_caro}")

    camionetas_mas_1000kg = contar_camionetas_mas_1000kg(vehiculos)
    print(f"Cantidad de camionetas con más de 1000 kg de capacidad de carga: {camionetas_mas_1000kg}")

    motos_alta_cilindrada = contar_motos_alta_cilindrada(vehiculos)
    print(f"Cantidad de motos de alta cilindrada: {motos_alta_cilindrada}")