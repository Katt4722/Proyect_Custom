class Clima:
    def __init__(self, temperatura=None, condicion=None):
        self.temperatura = temperatura
        self.condicion = condicion

    def determinar_tipo(self):
        """Determina si el clima es frio, templado o caluroso según la temperatura."""
        if self.temperatura is None:
            return "Desconocido"
        if self.temperatura < 15:
            return "Frio"
        elif 15 <= self.temperatura <= 25:
            return "Templado"
        else:
            return "Caluroso"
