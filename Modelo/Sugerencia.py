class Sugerencia:
    def __init__(self, motivo, outfit=None):
        self.motivo = motivo
        self.outfit = outfit

    def mostrar_sugerencia(self):
        """Muestra una sugerencia de outfit."""
        if self.outfit:
            return f"Sugerencia: {self.motivo} → {self.outfit.mostrar_outfit()}"
        return f"Sugerencia: {self.motivo}"
