import os
import telebot
from ChatBot.Core import Chatbot

# ⚙️ Configuración del token
# Guardalo en variable de entorno si podés, o ponelo directo para pruebas
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8282993521:AAEtXI_Dr5KgBmvWbKqtu2uk8k9nsX-hJrY")

# Crear instancia del bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)
# Instancia del chatbot que ya hiciste
chatbot = Chatbot()

# -----------------------
# Diccionarios de ejemplo
# -----------------------
ropa_combinaciones = {
    'remera blanca': ['chaqueta beige', 'zapatillas blancas 🩷'],
    'jean azul': ['remera blanca', 'sweater rosa 🌸'],
    'vestido rojo': ['zapatos negros', 'bolso beige ✨']
}

clima_outfits = {
    'soleado': ['vestido ligero', 'sandalias 🌞'],
    'lluvioso': ['impermeable', 'botas de agua ☔'],
    'frío': ['abrigo', 'bufanda 🧣'],
    'templado': ['camisa ligera', 'jean 🩷']
}

# -----------------------
# Menú inicial
# -----------------------
def mostrar_menu(chat_id):
    mensaje = (
        "¡Hola! 💕 Soy tu asistente de moda. ¿Qué querés hacer hoy?\n\n"
        "1️⃣ Sugerir outfit del día\n"
        "2️⃣ Ver combinaciones de colores\n"
        "3️⃣ Armar outfit con tu ropero 🌸\n"
        "4️⃣ Sugerir outfit según el clima ☀️🌧️❄️\n"
        "5️⃣ Salir 🩷"
    )
    bot.send_message(chat_id, mensaje)

# -----------------------
# Handler para /start
# -----------------------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "¡Hola! 💕 Soy tu asistente de moda. Vamos a brillar hoy ✨")
    mostrar_menu(message.chat.id)

# -----------------------
# Handler de opciones
# -----------------------
@bot.message_handler(func=lambda m: True)
def opciones(message):
    text = message.text.strip()

    # Opción 1: Sugerir outfit del día (aleatorio)
    if text == "1":
        outfit = "remera blanca y jean azul"
        bot.send_message(message.chat.id, f"Tu outfit del día podría ser: {outfit} ✨🩷")
        mostrar_menu(message.chat.id)

    # Opción 2: Combinaciones de colores
    elif text == "2":
        combinaciones = "Blanco combina con azul, negro y beige 🌸\nRojo combina con negro, blanco y dorado ✨"
        bot.send_message(message.chat.id, combinaciones)
        mostrar_menu(message.chat.id)

    # Opción 3: Armar outfit con tu ropero
    elif text == "3":
        msg = bot.send_message(message.chat.id, "¡Genial! ✨ Contame qué prendas tenés en mente o qué te gustaría usar.")
        bot.register_next_step_handler(msg, armar_outfit)

    # Opción 4: Outfit según el clima
    elif text == "4":
        msg = bot.send_message(message.chat.id, "¿Cómo está el clima hoy? (soleado, lluvioso, frío, templado)")
        bot.register_next_step_handler(msg, outfit_clima)

    # Opción 5: Salir
    elif text == "5":
        bot.send_message(message.chat.id, "¡Chau! 💖 Que tengas un día fashionista 🌸")
    else:
        bot.send_message(message.chat.id, "Ups 😅 no entendí tu opción, elegí un número del menú.")
        mostrar_menu(message.chat.id)

# -----------------------
# Función para armar outfit con ropa del usuario
# -----------------------
def armar_outfit(message):
    prendas_usuario = message.text.lower().split(",")  # separa por coma
    combinaciones = []

    for prenda in prendas_usuario:
        prenda = prenda.strip()
        if prenda in ropa_combinaciones:
            combinaciones += ropa_combinaciones[prenda]

    if combinaciones:
        combinaciones_str = ", ".join(set(combinaciones))
        bot.send_message(message.chat.id, f"Perfecto! 😊 Con eso podrías combinar {combinaciones_str} 🩷✨")
    else:
        bot.send_message(message.chat.id, "Mmm 😅 no tengo sugerencias para esas prendas, pero seguro se ve cute 💖")

    mostrar_menu(message.chat.id)

# -----------------------
# Función para outfit según clima
# -----------------------
def outfit_clima(message):
    clima = message.text.lower().strip()
    if clima in clima_outfits:
        outfit = ", ".join(clima_outfits[clima])
        bot.send_message(message.chat.id, f"Para un día {clima}, te recomiendo: {outfit} 🌸")
    else:
        bot.send_message(message.chat.id, "No entendí el clima 😅 Intenta con soleado, lluvioso, frío o templado 🩷")

    mostrar_menu(message.chat.id)

# -----------------------
# Arranque del bot
# -----------------------
if __name__ == "__main__":
    print("Bot de moda iniciado 💖✨")
    bot.infinity_polling()
