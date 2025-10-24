from Modelo.Usuario import Usuario
from Modelo.Prenda import Prenda
from Modelo.Outfit import Outfit
from Modelo.Color import Color
from Modelo.Clima import Clima
from Modelo.Sugerencia import Sugerencia

class Chatbot:
    def __init__(self):
        self.usuario = None

    def sugerir_outfit_texto(self):
        """Genera un outfit de ejemplo y devuelve el texto."""
        prenda1 = Prenda("remera", "blanca", "casual")
        prenda2 = Prenda("jean", "azul", "casual")
        outfit = Outfit("Outfit del día")
        outfit.agregar_prenda(prenda1)
        outfit.agregar_prenda(prenda2)
        return outfit.mostrar_outfit()

    def sugerir_colores_texto(self):
        """Devuelve un texto con una combinación de colores."""
        color1 = Color("rojo")
        color2 = Color("negro")
        return color1.combinar_con(color2)