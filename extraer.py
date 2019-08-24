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

a="""a) Las PC's de la empresa no pueden: i. Navegar por Redes Sociales.  ii. Leer los diarios.   iii. Realizar búsquedas en sitios de venta on line  iv. Compartir archivos por dropbox o similares  b) Debe asegurar búsquedas seguras c) La Notebook dirección puede navegar por cualquier lugar. Pero solo en horario  comercial (8 a 13 hs y 17 a 21 hs).  d) El servidor DNS solo puede realizar consultas DNS e) El servidor de Archivos no puede navegar. Se debe asegurar que no tenga acceso a  ningún protocolo hacia internet. f) El servidor de BD no puede navegar. g) No está permitido:  i.  las aplicaciones P2P  
"""
saltos = ["a\)","b\)","c\)","d\)"]

print(incertarSaltos(saltos, a))