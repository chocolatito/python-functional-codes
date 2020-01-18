import re
from functools import reduce

"""
Logica de una calculadora basica
que evalua expresiones aritmeticas '+', '-', '*' y '/'
"""


def sumar(expresion):
    return reduce(lambda a, b: a + b,
                  [restar(x) for x in re.split(r'\+', expresion)])


def restar(expresion):
    return reduce(lambda a, b: a - b,
                  [multiplicar(x) for x in re.split(r'\-', expresion)])


def multiplicar(expresion):
    return reduce(lambda a, b: a * b,
                  [dividir(x) for x in re.split(r'\*', expresion)])


def dividir(expresion):
    return reduce(lambda a, b: a / b,
                  [float(x) for x in re.split(r'\/', expresion)])


lst = sumar('2/1')
print(lst)
