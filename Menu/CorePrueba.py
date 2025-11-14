import sys
import os
import random

# Agrega la carpeta raíz del proyecto (Proyect_Custom) al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from transformers import pipeline

from Menu.Diccionarios import combinaciones, clima_outfits, accesorios

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Menu:
    def __init__(self, bot):

        self.bot = bot
        self.usuarios_estado = {}  # Diccionario para guardar estado de cada usuario.


    def mostrar_menu(self, user_id):
        self.bot.send_message(user_id, "¿Cómo seguimos? 🩷✨\n\n"
                                "1️⃣ Sugerir outfit del día\n"
                                "2️⃣ Ver combinaciones de colores\n"
                                "3️⃣ Armar outfit con tu ropero 🌸\n"
                                "4️⃣ Sugerir outfit según el clima ☀️🌧️❄️\n"
                                "5️⃣ Analizar sentimientos\n"
                                "6️⃣ Salir 🩷\n\n"
                                "🌻 Para tener una charla libre manda /charlar 🌻")

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
        elif estado == "clima":
            self.estado_clima(user_id, texto)
        elif estado == "analizar":
            self.estado_analizar(user_id, texto)
        elif estado == "accesorios":
            self.estado_accesorios(user_id, texto)

             
    # Estado principal del menú
    def estado_menu(self, user_id, texto):
        if texto == "1":
            self.bot.send_message(user_id, "✨ Generando outfit del día... ✨")
            
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
            colores = ", ".join(combinaciones.keys())
            self.bot.send_message(user_id, f"Podés combinar prendas según estos colores: {colores} 🌸\n"
                                    "Decime un color y te doy combinaciones cute ✨")

        elif texto == "3":
            # Armar outfit con tu ropero
            self.usuarios_estado[user_id]["estado"] = "armar_ropas"
            self.bot.send_message(user_id, "¡Genial! ✨ Contame qué prendas tenés en mente o qué te gustaría usar 🩷")

        elif texto == "4":
            # Outfit según clima
            self.usuarios_estado[user_id]["estado"] = "clima"
            self.bot.send_message(user_id, "Contame cómo está el clima hoy ☀️🌧️❄️ (lluvioso, humedo, frio, soleado)")

        elif texto == "5":
            self.usuarios_estado[user_id]["estado"] = "analizar"
            self.bot.send_message(user_id, "🌸✨Mandame un mensaje y analizare que sentimientos transmitis✨🌸")

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
            self.bot.send_message(user_id, f"No conozco combinaciones para {color} 😅 Pero espero que te quede cute! 💕")
        self.usuarios_estado[user_id]["estado"] = "menu"
        self.mostrar_menu(user_id)

    # Estado armar outfit con tu ropero
    def estado_armar_ropas(self, user_id, prendas_usuario):

        self.bot.send_message(user_id, f"Perfecto! 😊 Con eso podrías combinar zapatillas blancas o un blazer gris claro 🩷✨")
        self.bot.send_message(user_id, "¿Querés que te sugiera algún accesorio cute para completar el look? 🌸\n")
        self.usuarios_estado[user_id]["estado"] = "accesorios"

    #Estado elegir accesorios
    def estado_accesorios(self, user_id, respuesta):
        
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
                s
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

    #Estado analizar sentimientos
    def estado_analizar(self, user_id, frase):
        
        analizador_sentimiento = pipeline('sentiment-analysis', model = 'pysentimiento/robertuito-sentiment-analysis')
        
        resultado = analizador_sentimiento(frase)[0]

        sentimiento = resultado['label']
        confianza = resultado['score']

        if sentimiento.lower() == 'pos':
            sentimiento = 'Tu mensaje tiene un sentimiento positivo! espero que hoy tengas un lindo dia'
            emoji = '😊🌟'
        elif sentimiento.lower() == 'neu':
            sentimiento = 'Tu mensaje fue neutral...'
            emoji = '😐'
        elif sentimiento.lower() == 'neg':
            sentimiento = 'Detecto que hay sentimientos negativos, te recomiendo hablarlo con alguien con quien te sientas comodo!'
            emoji = '😞'
        else:
            emoji = 'H'

        self.bot.send_message(user_id, f"{sentimiento} {emoji}\n Tengo una confianza del {confianza:2%} en mi analisis")
        self.usuarios_estado[user_id]["estado"] = "menu"
        self.mostrar_menu(user_id)