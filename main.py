import os
import base64
import telebot
from groq import Groq
from dotenv import load_dotenv

# =======================
# 1️⃣ Cargar variables .env
# =======================
env_path = r"C:\Users\Equipo\Documents\proyecto samsung\Proyect_Custom\.env"
load_dotenv(dotenv_path=env_path)

TOKEN_BOT_TELEGRAM = os.getenv("TELEGRAM_BOT_TOKEN")
CLAVE_API_GROQ = os.getenv("GROQ_API_KEY")

print("🔍 TOKEN encontrado:", TOKEN_BOT_TELEGRAM)
print("🔍 CLAVE API GROQ encontrada:", CLAVE_API_GROQ)

if not TOKEN_BOT_TELEGRAM:
    raise ValueError("TELEGRAM_BOT_TOKEN no está configurado en las variables de entorno")

if not CLAVE_API_GROQ:
    raise ValueError("GROQ_API_KEY no está configurado en las variables de entorno")

# =======================
# 2️⃣ Inicializar bot y cliente Groq
# =======================
bot = telebot.TeleBot(TOKEN_BOT_TELEGRAM)
cliente_groq = Groq(api_key=CLAVE_API_GROQ)

# =======================
# 3️⃣ Prompt base para el análisis de moda
# =======================
PROMPT_ASESOR_MODA = """
Eres un Asesor de Moda Personal experto en estilo, colorimetría y comercio electrónico. 
Tu tarea es analizar la imagen proporcionada por el usuario y generar una respuesta concisa y útil siguiendo los siguientes pasos:

1. **ANÁLISIS DE LA IMAGEN:**
   - Identifica la(s) prenda(s) principal(es) que lleva la persona.
   - Determina los colores predominantes en la vestimenta y el tono de piel para la colorimetría.
   - Evalúa el estilo general (casual, formal, deportivo, etc.).

2. **RECOMENDACIONES DE COMBINACIÓN Y COLORIMETRÍA:**
   - Propón **3 prendas o accesorios** que combinan perfectamente con lo que lleva puesto.
   - Sugiere una **paleta de 3 colores** que realzan la prenda principal y que complementan bien a la persona (justifica brevemente por qué).

3. **RECOMENDACIONES DE PRODUCTOS SIMILARES EN EL MERCADO (BUSCADOR):**
   - Proporciona el **Nombre del Producto, la Marca y un Enlace de compra válido**.
"""

# =======================
# 4️⃣ Respuesta a /start
# =======================
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "👋 ¡Hola! Soy tu asesor de moda virtual. Envíame una foto de tu atuendo y te daré recomendaciones personalizadas de estilo y colorimetría. 💃🕺")

# =======================
# 5️⃣ Procesar imágenes
# =======================
@bot.message_handler(content_types=["photo"])
def analizar_imagen(message):
    try:
        # Descargar la foto enviada
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Convertir la imagen a base64
        image_base64 = base64.b64encode(downloaded_file).decode("utf-8")

        bot.reply_to(message, "🔎 Analizando tu outfit... Esto puede tardar unos segundos 👗")

        # Enviar imagen al modelo de Groq
        response = cliente_groq.chat.completions.create(
            model="llava-v1.6-34b",  # Usar modelo visual disponible
            messages=[
                {"role": "system", "content": PROMPT_ASESOR_MODA},
                {"role": "user", "content": [
                    {"type": "text", "text": "Analiza esta imagen y aplica el prompt anterior."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                ]}
            ],
        )

        # Extraer la respuesta generada
        resultado = response.choices[0].message["content"]
        bot.reply_to(message, f"🧥 **Análisis de Estilo:**\n\n{resultado}")

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error al procesar la imagen: {e}")

# =======================
# 6️⃣ Ejecutar el bot
# =======================
print("🤖 Bot de asesor de moda iniciado correctamente...")
bot.polling()
