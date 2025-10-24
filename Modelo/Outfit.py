class Outfit:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prendas = []
        self.descripcion = ""
        self.es_favorito = False

    def agregar_prenda(self, prenda):
        """Agrega una prenda al outfit."""
        self.prendas.append(prenda)

    def mostrar_outfit(self):
        """Devuelve el listado de prendas que componen el outfit."""
        prendas_texto = ", ".join([p.mostrar_prenda() for p in self.prendas])
        return f"Outfit '{self.nombre}': {prendas_texto}"

    def marcar_favorito(self):
        """Marca el outfit como favorito."""
        self.es_favorito = True
