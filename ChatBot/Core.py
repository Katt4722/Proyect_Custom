from Modelo.Usuario import Usuario
from Modelo.Prenda import Prenda
from Modelo.Outfit import Outfit
from Modelo.Color import Color
from Modelo.Clima import Clima
from Modelo.Sugerencia import Sugerencia
from ChatBot.Diccionarios import prendas, combinaciones, clima_outfits, accesorios
import random

class Menu: 
    def __init__(self, bot):
        self.bot = bot
        self.usuarios_estado = {}

    def mostrar_menu(self, user_id):
        self.bot.send_message(user_id, "¿Cómo seguimos? 🩷✨\n\n"
                              "1️⃣ Sugerir outfit del día\n"
                              "2️⃣ Ver combinaciones de colores\n"
                              "3️⃣ Armar outfit con tu guardaropa 🌸\n"
                              "4️⃣ Sugerir outfit según el clima ☀️🌧️❄️\n"
                              "5️⃣ Salir 🩷")

    def responder(self, user_id, texto):

        if user_id not in self.usuarios_estado:
            self.usuarios_estado[user_id] = {"estado": "menu", "usuario": Usuario(nombre=f"Usuario_{user_id}")}

        estado = self.usuarios_estado[user_id]["estado"]
        texto = texto.lower()

    # Estado del usuario
        if estado == "menu":
            self.estado_menu(user_id, texto)
        elif estado == "combinaciones_colores":
            self.estado_combinaciones_colores(user_id, texto)
        elif estado == "armar_ropas":
            self.estado_armar_ropas(user_id, texto)
        elif estado == "accesorios":
            self.estado_accesorios(user_id, texto)
        elif estado == "clima":
            self.estado_clima(user_id, texto)
    #elif estado == "analizar":
        #self.estado_analizar(user_id, texto)

    # Estado principal del menú 
    def estado_menu(self, user_id, texto):
        if texto == "1":
            
            tops = ["remera", "blusa", "camisa", "buzo", "sweater", "top"]
            bottoms = ["jean", "pantalón", "falda", "short", "pollera"]
            calzados = ["zapatillas", "botas", "sandalias", "zapatos"]
            extras = ["chaqueta", "saco", "blazer", "abrigo"]

            colores = [
                "blanco", "negro", "rosa", "celeste", "beige", 
                "gris", "lila", "verde oliva", "azul marino"
            ]
            estilos = ["casual", "urbano", "elegante", "deportivo", "chic"]

            # Elegir prendas al azar
            prenda_top = random.choice(tops)
            prenda_bottom = random.choice(bottoms)
            prenda_calzado = random.choice(calzados)
            color_top = random.choice(colores)
            color_bottom = random.choice(colores)
            color_calzado = random.choice(colores)
            estilo = random.choice(estilos)

            descripcion = (
                f"Outfit del día 🌸✨\n\n"
                f"👚 {prenda_top.capitalize()} {color_top}, "
                f"👖 {prenda_bottom} {color_bottom} y "
                f"👟 {prenda_calzado} {color_calzado}.\n\n"
                f"Estilo: {estilo.capitalize()} 💖."
            )

            self.bot.send_message(user_id, descripcion)
            self.mostrar_menu(user_id)

        elif texto == "2":
            # Combinaciones de colores
            self.usuarios_estado[user_id]["estado"] = "combinaciones_colores"
            colores = ", ".join(prendas.keys())
            self.bot.send_message(user_id, f"Podés combinar prendas según estos colores: {colores} 🌸\n"
                                      "Por ejemplo, podés decirme un color y te doy combinaciones cute ✨")

        elif texto == "3":
            # Armar outfit con tu ropero
            self.usuarios_estado[user_id]["estado"] = "armar_ropas"
            self.bot.send_message(user_id, "¡Genial! ✨ Contame qué prendas tenés en mente o qué te gustaría usar 🩷")

        elif texto == "4":
            # Outfit según clima
            self.usuarios_estado[user_id]["estado"] = "clima"
            self.bot.send_message(user_id, "Contame cómo está el clima hoy ☀️🌧️❄️ (ej: Húmedo, Frío, Soleado)")

        elif texto == "5":
            self.bot.send_message(user_id, "Bye! 🩷 ¡Que tengas un día fashionista! ✨")
            self.usuarios_estado.pop(user_id)

        else:
            self.bot.send_message(user_id, "Ups 😅 no entendí, elegí una opción del menú 🩷")
            self.mostrar_menu(user_id)

    # Estado combinaciones de colores
    def estado_combinaciones_colores(self, user_id, texto):
        color = texto.lower()
        if color in combinaciones:
            sugerencias = ", ".join(combinaciones[color])
            self.bot.send_message(user_id, f"Con el color {color} podrías combinar: {sugerencias} 🌸✨")
            self.usuarios_estado[user_id]["estado"] = "menu"
            self.mostrar_menu(user_id)
        else:
            self.bot.send_message(user_id, f"No conozco combinaciones para {color} 😅, pero espero que te quede cute! 💕")
            self.usuarios_estado[user_id]["estado"] = "menu"
            self.mostrar_menu(user_id)


    # Estado armar outfit con tu guardaropa
    def estado_armar_ropas(self, user_id, texto):
        prenda = texto.lower()
        self.bot.send_message(user_id, f"Perfecto! 😊 Con eso podrías combinar zapatillas blancas o un blazer gris claro 🩷✨")
        self.bot.send_message(user_id, "¿Querés que te sugiera algún accesorio cute para completar el look? 🌸\n")
        self.usuarios_estado[user_id]["estado"] = "accesorios"

    def estado_accesorios(self, user_id, texto):
        respuesta = texto.lower()
        
        if "sí" in respuesta or "si" in respuesta:
            sugerencia = random.choice(accesorios)
            self.bot.send_message(user_id, f"Podrías usar {sugerencia} 💕 ¡queda súper lindo con tu look!")
        else:
            self.bot.send_message(user_id, "¡Perfecto! 🩷 A veces menos es más 😌✨")

        self.bot.send_message(user_id, "¡Qué bello outfit armamos! 🌸✨")
        self.usuarios_estado[user_id]["estado"] = "menu"
        self.mostrar_menu(user_id)

    # Estado clima
    def estado_clima(self, user_id, texto):
        def normalizar(s):
            return (
                s.lower()
                .replace("á", "a")
                .replace("é", "e")
                .replace("í", "i")
                .replace("ó", "o")
                .replace("ú", "u")
            )

        clima = normalizar(texto)
    
        clima_outfits_normalizado = {normalizar(k): v for k, v in clima_outfits.items()}

        if clima in clima_outfits_normalizado:
            outfit = clima_outfits_normalizado[clima]
            self.bot.send_message(user_id, f"Hoy está {texto.lower()}, te recomiendo usar: {', '.join(outfit)} 🌸✨")
        else:
            self.bot.send_message(user_id, "No estoy segura de ese clima 😅 pero igual podés usar algo cute y cómodo 💕")

        self.usuarios_estado[user_id]["estado"] = "menu"
        self.mostrar_menu(user_id)