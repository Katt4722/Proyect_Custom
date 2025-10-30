import sys
import os

# Agrega la carpeta raíz del proyecto (Proyect_Custom) al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from transformers import pipeline

from Modelo.Usuario import Usuario
from Modelo.Prenda import Prenda
from Modelo.Outfit import Outfit
from Modelo.Color import Color
from Modelo.Clima import Clima
from Modelo.Sugerencia import Sugerencia
from ChatBot.Diccionarios import prendas, combinaciones, clima_outfits, accesorios

class Menu:
    def __init__(self, bot):

        self.bot = bot
        self.usuarios_estado = {}  # Diccionario para guardar estado de cada usuario. Atributo de Menu

        #self.stickers_cute = [
        #    "CAACAgIAAxkBAAEHk2Fg1b9Xl2Z5fVtRQJZc9nRV1vOYGgACXQADwDZPE0G1t9V5uN7zIwQ",  # gatito
        #    "CAACAgIAAxkBAAEHk2Ng1b9XqfO3JrtUoxv4zFQK5iY6JwACXgADwDZPE3lF8jl0g5q0IwQ",  # corazon rosa
        #    "CAACAgIAAxkBAAEHk2Vg1b9XrT3H6L5KksMshIFXSh-8gACYAADwDZPE2Zw8Ct5V_2VIwQ",  # moñito
        #]

    def mostrar_menu(self, user_id):
        self.bot.send_message(user_id, "¿Cómo seguimos? 🩷✨\n\n"
                                "1️⃣ Sugerir outfit del día\n"
                                "2️⃣ Ver combinaciones de colores\n"
                                "3️⃣ Armar outfit con tu ropero 🌸\n"
                                "4️⃣ Sugerir outfit según el clima ☀️🌧️❄️\n"
                                "5️⃣ Analizar sentimientos\n"
                                "6️⃣ Salir 🩷") 

    def responder(self, user_id, texto):
        
        if user_id not in self.usuarios_estado:
            self.usuarios_estado[user_id] = {"estado": "menu", "usuario": Usuario("Provisorio")} #en vez de 1 ahi decia "usuario" : Usuario()

        estado = self.usuarios_estado[user_id]["estado"]
        texto = texto.lower()

        # Estado del usuario
        if estado == "menu":
            self.estado_menu(user_id, texto)
        elif estado == "combinaciones_colores":
            self.estado_combinaciones_colores(user_id, texto)
        elif estado == "armar_ropas":
            self.estado_armar_ropas(user_id, texto)
        elif estado == "clima":
            self.estado_clima(user_id, texto)
        elif estado == "analizar":
            self.estado_analizar(user_id, texto)
             

    def estado_menu(self, user_id, texto):
            if texto == "1":
                self.bot.send_message(user_id, "✨ Generando outfit del día... ✨")
                prenda1 = Prenda("remera", "blanca", "casual")
                prenda2 = Prenda("jean", "azul", "casual")
                outfit = Outfit("Outfit del día")
                outfit.agregar_prenda(prenda1)
                outfit.agregar_prenda(prenda2)
                self.bot.send_message(user_id, f"{outfit.mostrar_outfit()} 🩷✨")
            # En caso de que fallen los stickers, descomentar esta línea:
            # bot.send_sticker(user_id, random.choice(stickers_cute))
                self.mostrar_menu(user_id)

            elif texto == "2":
                # Combinaciones de colores
                self.usuarios_estado[user_id]["estado"] = "combinaciones_colores"
                colores = ", ".join(combinaciones.keys())
                self.bot.send_message(user_id, f"Podés combinar prendas según estos colores: {colores} 🌸\n"
                                        "Por ejemplo, podés decirme un color y te doy combinaciones cute ✨")

            elif texto == "3":
                # Armar outfit con tu ropero
                self.usuarios_estado[user_id]["estado"] = "armar_ropas"
                self.bot.send_message(user_id, "¡Genial! ✨ Contame qué prendas tenés en mente o qué te gustaría usar 🩷")

            elif texto == "4":
                # Outfit según clima
                self.usuarios_estado[user_id]["estado"] = "clima"
                self.bot.send_message(user_id, "Contame cómo está el clima hoy ☀️🌧️❄️ (ej: húmedo, frío, soleado)")

            elif texto == "5":
                self.usuarios_estado[user_id]["estado"] = "analizar"
                self.bot.send_message(user_id, "Mandame un mensaje y analizare que sentimientos transmite!")

            elif texto == "6":
                self.bot.send_message(user_id, "Bye! 🩷 ¡Que tengas un día fashionista! ✨")
                self.usuarios_estado.pop(user_id)

            else:
                self.bot.send_message(user_id, "Ups 😅 no entendí, elegí una opción del menú 🩷")
                self.mostrar_menu(user_id)

        # Estado combinaciones de colores
    def estado_combinaciones_colores(self, user_id, color): #color va a ser igual a texto.lower()
            if color in combinaciones:
                sugerencias = ", ".join(combinaciones[color])
                self.bot.send_message(user_id, f"Con el color {color} podrías combinar: {sugerencias} 🌸✨")
            else:
                self.bot.send_message(user_id, f"No conozco combinaciones para {color} 😅 Pero igual podemos probar algo cute! 💕")
            self.usuarios_estado[user_id]["estado"] = "menu"
            self.mostrar_menu(user_id)

        # Estado armar outfit con tu ropero
    def estado_armar_ropas(self, user_id, prendas_usuario):

            self.bot.send_message(user_id, f"Perfecto! 😊 Con eso podrías combinar zapatillas blancas o un blazer gris claro 🩷✨")
            self.bot.send_message(user_id, "¿Querés que te sugiera algún accesorio cute para completar el look? 🌸\n"
                                "Elegí clima: frio, calido, soleado, lluvia, humedo")
            self.usuarios_estado[user_id]["estado"] = "clima"


        # Estado clima
    def estado_clima(self, user_id, clima):

            if clima in clima_outfits:
                outfit = clima_outfits[clima]
                self.bot.send_message(user_id, f"Hoy está {clima}, entonces te recomiendo: {', '.join(outfit)} 🌸✨")
            else:
                self.bot.send_message(user_id, "No estoy segura de ese clima 😅 pero igual podés usar algo cute y cómodo 💕")
            self.usuarios_estado[user_id]["estado"] = "menu"
            self.mostrar_menu(user_id) 
            
    def estado_analizar(self, user_id, frase):
        
        analizador_sentimiento = pipeline('sentiment-analysis', model = 'pysentimiento/robertuito-sentiment-analysis')
        
        resultado = analizador_sentimiento(frase)[0]

        sentimiento = resultado['label']  #traigo la etiqueta label y score
        confianza = resultado['score']

        if sentimiento.lower() == 'pos':
            sentimiento = 'Tu mensaje tiene un sentimiento positivo! espero que hoy tengas un lindo dia'
            emoji = ':)'
        elif sentimiento.lower() == 'neu':
            sentimiento = 'Tu mensaje fue neutral...'
            emoji = ':|'
        elif sentimiento.lower() == 'neg':
            sentimiento = 'Detecto que hay sentimientos negativos, te recomiendo hablarlo con alguien con quien te sientas comodo!'
            emoji = ':('
        else:
            emoji = 'H'

        self.bot.send_message(user_id, f"{sentimiento} {emoji}\n Tengo una confianza del {confianza:2%} en mi analisis") #El bot le manda al usuario el analisis de sentimiento de su mensaje 
        self.usuarios_estado[user_id]["estado"] = "menu"
        self.mostrar_menu(user_id)

