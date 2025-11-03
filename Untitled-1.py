class ListaDeUtiles:


def __init__(self, valor, unidades, utilidad):
# Atributos Privados
self.__valor = valor
self.__unidades = unidades

# Atributo Público
self.utilidad = utilidad


def mostrar_info(self):

print("--- Información del Útil ---")

print(f"Valor Unitario: ${self.__valor}")
print(f"Cantidad: {self.__unidades}")

print(f"Utilidad: {self.utilidad}")
print(f"Costo Total: ${self.calcular_costo_total()}")
print("----------------------------")

#publico
def calcular_costo_total(self):
"""Calcula el costo total usando los atributos privados."""
return self.__valor * self.__unidades

lapiz = ListaDeUtiles(5, 10, "Escribir y dibujar")
#este es publico
print(f"La utilidad del lápiz es: {lapiz.utilidad}")
#aca como es privado pedimos la info y accede a ella
lapiz.mostrar_info()
#aca genera error por que lo llamas directamente
print(f"lapiz es {lapiz.__valor}")
