import random
import functools

numeros = list(map(lambda _: random.randint(-1000000, 1000000), range(1000)))


menor = functools.reduce(lambda x, y: x if x < y else y, numeros)

pares = len(list(filter(lambda x: x % 2 == 0, numeros)))

print(str(pares))

impares = list(filter(lambda x: x % 2 != 0, numeros))

promedio_impares = functools.reduce(lambda x, y: x + y, impares) / len(impares)

# Filtrar números entre 10 y 100 y calcular sus cuadrados
cuadrados = list(map(lambda x: x ** 2, filter(lambda x: 10 < x < 100, numeros)))

print(cuadrados)

multiplos_3 = list(filter(lambda x: x % 3 == 0, list(cuadrados)))

print(multiplos_3)

multiplos_7 = list(filter(lambda x: x % 7 == 0, numeros))
multiplos_7_ord = sorted(multiplos_7, reverse=True)

print(multiplos_7_ord)

impares_negativos = list(filter(lambda x: x < 0, impares))

suma = sum(numeros)
promedio = suma / len(numeros)

desviacion_est = (functools.reduce(lambda x, y: x + y, list(map(lambda x: (x - promedio) ** 2, impares))) / len(impares)) ** 0.5
print(desviacion_est)

existe_multiplo_127 = any(map(lambda x: x % 127 == 0, numeros))

print(f"¿Existe algún múltiplo de 127? {'Sí' if existe_multiplo_127 else 'No'}")

termina_en_2_o_3 = list(filter(lambda x: str(x)[-1] in ['2', '3'], numeros))

print(termina_en_2_o_3)