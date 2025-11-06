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
import json
import random

from ChatBot.Core import Menu

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_API_KEY","8336358155:AAHkwdN4i6zbW-5af3Gp7LAZwYMjqUIaEz4")
GROQ_API_KEY = os.getenv("GROQ_API_KEY","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")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)


# Cargar datos (por ejemplo, combinaciones o tendencias)
def load_fashion_data():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "fashion_dataset.json")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Error al cargar el dataset: {str(e)}")
        return None

fashion_data = load_fashion_data()

# -----------------------
# Funciones auxiliares
# -----------------------

def get_groq_fashion_response(user_message: str):
    try:
        system_prompt = """Eres un asesor virtual de moda y estilo 👗🕶️.
Ayuda al usuario a combinar prendas, elegir outfits o colores según ocasión o clima."""

        chat_completion = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.6,
            max_tokens=600
        )

        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error al obtener respuesta de Groq: {str(e)}")
        return None


def transcribe_voice_with_groq(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        print(f"🎙️ Archivo recibido: {file_info.file_path}")
        downloaded_file = bot.download_file(file_info.file_path)

        temp_file = "temp_voice.ogg"

        with open(temp_file, "wb") as f:
            f.write(downloaded_file)

        print("📤 Enviando a Whisper para transcripción...")
        with open(temp_file, "rb") as file:
            transcription = groq_client.audio.transcriptions.create(
                file=(temp_file, file.read()),
                model="whisper-large-v3-turbo",
                response_format="json",
                language="es"
            )

        os.remove(temp_file)

        text = transcription.text.strip()
        print(f"✅ Transcripción recibida: {text}")
        return text

    except Exception as e:
        print(f"❌ Error al transcribir: {str(e)}")
        return None


@bot.message_handler(content_types=["voice"])
def handle_voice(message):
    processing_msg = bot.reply_to(message, "✨ Estoy escuchando tu audio... dame un segundito para encontrar tu look perfecto 🩷🌸")

    transcription = transcribe_voice_with_groq(message)
    if not transcription:
        bot.edit_message_text(
            "😅 Ups… no pude entender tu audio. ¿Podés intentar de nuevo? 🌸",
            chat_id=message.chat.id, 
            message_id=processing_msg.message_id
        )
        return

    print(f"📝 Texto detectado: {transcription}")

    response = get_groq_fashion_response(transcription)
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


# -----------------------
# Handlers
# -----------------------

menu_principal = Menu(bot)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, "¡Hola! 💕 Soy tu asistente de moda. Vamos a brillar hoy ✨")
    menu_principal.mostrar_menu(user_id)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_id = message.from_user.id
    texto = message.text.strip()
    menu_principal.responder(user_id, texto)

# Manejo de voz


# -----------------------
# Inicio del bot
# -----------------------
if __name__ == "__main__":
    print("Bot de moda iniciado 🩷✨")
    bot.infinity_polling()
