import telebot as tlb
import os
import json
from groq import Groq
from typing import Optional
import time
from dotenv import load_dotenv

user_histories = {}  # Aquí guardaremos el historial de cada usuario

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Instanciar clientes
bot = tlb.TeleBot(TELEGRAM_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

class AsistenteVoz: 
    def __init__(self, bot, groq_client):
        self.bot = bot
        self.groq_client = groq_client


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


def get_groq_fashion_response(user_id: int, new_user_message: str):

    try:
        system_prompt = f"""Eres un asesor virtual de moda y estilo 👗🕶️.
Tu tarea es ayudar al usuario a elegir combinaciones de ropa, colores, estilos o outfits 
basándote en las tendencias de moda, y en los siguientes datos de ejemplo:

{json.dumps(fashion_data, ensure_ascii=False, indent=2)}

Reglas importantes:
1. Sé amable, cercano y profesional, como un estilista personal.
2. Explica brevemente el porqué de tus recomendaciones.
3. Usa un tono motivador y elegante, con emojis de moda o colores.
4. Si el usuario menciona una ocasión (ej: boda, entrevista, cena, playa), adapta la recomendación al contexto.
5. Si no entiende bien la pregunta, pide más detalles.
6. Si el usuario pide que te explayes más, recordá lo último que le dijiste y desarrollá tu explicación.
7. No inventes marcas ni precios si no están en el dataset."""

        # Obtener historial del usuario
        historial = user_histories.get(user_id, [])

        # Construir el listado de mensajes con roles reales
        mensajes = [{"role": "system", "content": system_prompt}]
        mensajes.extend(historial)  # agrega los mensajes anteriores del usuario y asistente
        mensajes.append({"role": "user", "content": new_user_message})  # agrega el mensaje actual

        chat_completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=mensajes,
            temperature=0.6,
            max_tokens=600
        )

        response_text = chat_completion.choices[0].message.content.strip()
        return response_text

    except Exception as e:
        print(f"❌ Error al obtener respuesta de Groq: {str(e)}")
        return None



def transcribe_voice_with_groq(message: tlb.types.Message) -> Optional[str]:
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        temp_file = "temp_voice.ogg"

        # Guardar audio temporalmente
        with open(temp_file, "wb") as f:
            f.write(downloaded_file)

        # Transcribir audio con Groq
        with open(temp_file, "rb") as file:
            transcription = groq_client.audio.transcriptions.create(
                file=(temp_file, file.read()),
                model="whisper-large-v3-turbo",
                prompt="Transcribe un audio en español sobre moda o estilo personal.",
                response_format="json",
                language="es"
            )

        os.remove(temp_file)

        text = transcription.get("text", "").strip()
        return text
    except Exception as e:
        print(f"🎧 Error al transcribir el audio: {str(e)}")
        return None


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: tlb.types.Message):
    welcome_text = (
        "👋 ¡Hola! Soy tu asistente de moda virtual.\n\n"
        "Puedo ayudarte a combinar colores, elegir outfits o encontrar tu estilo.\n"
        "✨ Enviame un mensaje o incluso una nota de voz contándome qué querés ponerte hoy."
    )
    bot.reply_to(message, welcome_text)



@bot.message_handler(content_types=["text"])
def handle_text(message: tlb.types.Message):
    bot.send_chat_action(message.chat.id, 'typing')
    response = get_groq_fashion_response(message.text)
    if response:
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Lo siento, hubo un error al procesar tu mensaje. Intenta nuevamente 💬")



@bot.message_handler(content_types=["voice"])
def handle_voice(message: tlb.types.Message):
    user_id = message.from_user.id
    bot.send_chat_action(message.chat.id, 'typing')

    # Transcribir audio
    transcription = transcribe_voice_with_groq(message)
    if not transcription:
        bot.reply_to(message, "⚠️ No pude transcribir tu audio, por favor intenta de nuevo.")
        return

    # Guarda en historial
    if user_id not in user_histories:
        user_histories[user_id] = []
    user_histories[user_id].append({"role": "user", "content": transcription})

    # Genera una respuesta usando el historial
    historial = user_histories[user_id]
    response = get_groq_fashion_response(" ".join([m["content"] for m in historial if m["role"]=="user"]))

    # Guarda la respuesta en historial
    user_histories[user_id].append({"role": "assistant", "content": response})

    # Envía respuesta
    if response:
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "❌ No pude procesar tu consulta. Intenta nuevamente más tarde.")

