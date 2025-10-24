class Prenda:
    def __init__(self, tipo, color, estilo=None, material=None, clima_apropiado=None):
        self.tipo = tipo
        self.color = color
        self.estilo = estilo
        self.material = material
        self.clima_apropiado = clima_apropiado

    def mostrar_prenda(self):
        """Devuelve una descripción de la prenda."""
        return f"{self.tipo} de color {self.color} (estilo: {self.estilo})"

    def es_apta_para_clima(self, clima):
        """Verifica si la prenda es adecuada para un tipo de clima."""
        return self.clima_apropiado == clima
