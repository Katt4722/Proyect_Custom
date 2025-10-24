import os
import telebot
import random
from ChatBot.Core import responder, mostrar_menu, usuarios_estado

# ⚙️ Configuración del token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8282993521:AAEtXI_Dr5KgBmvWbKqtu2uk8k9nsX-hJrY")

# Crear instancia del bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# -----------------------
# Handlers
# -----------------------
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in usuarios_estado:
        usuarios_estado[user_id] = {"estado": "menu"}
    bot.send_message(user_id, "¡Hola! 💕 Soy tu asistente de moda. Vamos a brillar hoy ✨")
    mostrar_menu(bot, user_id)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_id = message.from_user.id
    texto = message.text.strip()

    # Llamamos a la función responder de Core.py
    responder(bot, user_id, texto)

# -----------------------
# Inicio del bot
# -----------------------
if __name__ == "__main__":
    print("Bot de moda iniciado 🩷✨")
    bot.infinity_polling()
