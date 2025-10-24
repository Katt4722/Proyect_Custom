class Usuario:
    def __init__(self, nombre, genero=None, estilo_preferido=None, ciudad=None):
        self.nombre = nombre
        self.genero = genero
        self.estilo_preferido = estilo_preferido
        self.ciudad = ciudad
        self.prendas = []
        self.outfits = []

    def agregar_prenda(self, prenda):
        """Agrega una prenda al guardarropa del usuario."""
        self.prendas.append(prenda)

    def guardar_outfit(self, outfit):
        """Guarda un outfit en la lista del usuario."""
        self.outfits.append(outfit)

    def obtener_prendas(self):
        """Devuelve todas las prendas del usuario."""
        return self.prendas

    def mostrar_info(self):
        """Muestra los datos básicos del usuario."""
        return f"Usuario: {self.nombre} | Estilo: {self.estilo_preferido} | Ciudad: {self.ciudad}"
