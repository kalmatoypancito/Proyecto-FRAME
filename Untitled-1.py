class lista_de_utiles:
    def __init__(self, valor, unidades, utilidad):
        self.valor = valor          # Precio o valor del útil
        self.unidades = unidades    # Cantidad
        self.utilidad = utilidad    # Para qué sirve

    def mostrar_info(self):
        print(f"Valor: ${self.valor}")
        print(f"Unidades: {self.unidades}")
        print(f"Utilidad: {self.utilidad}")

# Ejemplo de uso
lapiz = lista_de_utiles(5, 10, "Escribir y dibujar")
lapiz.mostrar_info()