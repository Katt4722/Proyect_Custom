class Color:
    def __init__(self, nombre, codigo_hex=None):
        self.nombre = nombre
        self.codigo_hex = codigo_hex

    def combinar_con(self, otro_color):
        """Devuelve un texto con una sugerencia de combinación."""
        return f"El color {self.nombre} combina bien con {otro_color.nombre}."
