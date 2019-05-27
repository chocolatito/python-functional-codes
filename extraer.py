from functools import *
import re
"""

1.1.1 The primary activities of software engineering
"""

def incertarSaltos(saltos, texto):
	if saltos:
		return incertarSaltos(saltos[1:], "".join(re.sub(saltos[0],"\n"+saltos[0],texto)))
	else:
		return texto


def quitarSalto(texto):
	return "".join(re.sub("\n"," ",texto))

a="""
"""
saltos = []

#print(incertarSaltos(saltos, a))
print(quitarSalto(a))