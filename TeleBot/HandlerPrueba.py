#Agregue esto porque Python no encontraba las otras carpetas-----------------------------
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
#-------------------------------------------------------------------------------------

import telebot
from groq import Groq
from dotenv import load_dotenv
from ChatBot.CorePrueba import Menu
from AnalisisVoz.AnalizarVoz import AnalizarVoz
from AnalisisDeImagen.AnalizarImagen import AnalizarImagen

from Modelo.Usuario import Usuario

load_dotenv()

# ⚙️ Configuración del token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_API_KEY", "8336358155:AAHkwdN4i6zbW-5af3Gp7LAZwYMjqUIaEz4")
GROQ_API_KEY = os.getenv("GROQ_API_KEY","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")

# Crear instancia del bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

menu_principal = Menu(bot)
analisis_de_voz = AnalizarVoz(bot, groq_client)
analisis_de_imagen = AnalizarImagen(bot, groq_client)

# -----------------------
# Handlers
# -----------------------

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, "¡Hola! 💕 Soy tu asistente de moda. Vamos a brillar hoy ✨")
    menu_principal.mostrar_menu(user_id)

@bot.message_handler(commands=['charlar'])
def conversacion(message):
    user_id = message.from_user.id

    bot.send_message(user_id, "Vamos a charlar sobre moda! Dejame tus consultas o pedime lo que necesites al respecto")
    bot.register_next_step_handler(message, continuar_conversacion)

def continuar_conversacion(message):
    user_id = message.from_user.id
    texto = message.text.strip()

    if texto == "/salir":
        bot.send_message(user_id, "¡Gracias por la charla! ✨🩷 Si querés volver al menú, usa /start")
        return

    respuesta = analisis_de_voz.get_groq_fashion_response(texto)

    bot.send_message(user_id, respuesta)
    bot.register_next_step_handler(message, continuar_conversacion)

@bot.message_handler(func=lambda m: True)
def menu(message):
    user_id = message.from_user.id
    texto = message.text.strip()
   
    # Llamamos a la función responder de CorePrueba.py
    menu_principal.responder(user_id, texto)

@bot.message_handler(content_types=["voice"])
def handle_voice(message):
    processing_msg = bot.reply_to(message, "✨ Estoy escuchando tu audio... dame un segundito para encontrar tu look perfecto 🩷🌸")

    transcription = analisis_de_voz.transcribe_voice_with_groq(message)
    if not transcription:
        bot.edit_message_text(
            "😅 Ups… no pude entender tu audio. ¿Podés intentar de nuevo? 🌸",
            chat_id=message.chat.id, 
            message_id=processing_msg.message_id
        )
        return

    print(f"📝 Texto detectado: {transcription}")

    response = analisis_de_voz.get_groq_fashion_response(transcription)
    if response:
        bot.edit_message_text(
            f"👗 Tu outfit del día: {response} 🌸✨",
            chat_id=message.chat.id, 
            message_id=processing_msg.message_id
        )
    else:
        bot.edit_message_text(
            "🌸 Lo siento, no pude generar tu outfit 😢 ¡Probemos otra vez! 👗✨",
            chat_id=message.chat.id,
            message_id=processing_msg.message_id
        )

@bot.message_handler(content_types=["photo"])
def handler_image(message):
    analisis_de_imagen.analizar_imagen(message)

# -----------------------
# Inicio del bot
# -----------------------

if __name__ == "__main__":
    print("Bot de moda iniciado 🩷✨")
    bot.infinity_polling()