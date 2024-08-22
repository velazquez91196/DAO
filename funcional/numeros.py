import random
import functools

numeros = list(map(lambda _: random.randint(-1000000, 1000000), range(1000)))


menor = functools.reduce(lambda x, y: x if x < y else y, numeros)

pares = 
