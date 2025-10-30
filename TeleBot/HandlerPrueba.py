#Agregue esto porque Python no encontraba las otras carpetas-----------------------------

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
#-------------------------------------------------------------------------------------

import telebot
import random
from ChatBot.CorePrueba import Menu
from Modelo.Usuario import Usuario


# ⚙️ Configuración del token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8336358155:AAHkwdN4i6zbW-5af3Gp7LAZwYMjqUIaEz4")

# Crear instancia del bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)
menu_principal = Menu(bot)

# -----------------------
# Handlers
# -----------------------

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, "¡Hola! 💕 Soy tu asistente de moda. Vamos a brillar hoy ✨")
    menu_principal.mostrar_menu(user_id)

@bot.message_handler(func=lambda m: True)
def menu(message):
    user_id = message.from_user.id
    texto = message.text.strip()
   
    # Llamamos a la función responder de CorePrueba.py
    menu_principal.responder(user_id, texto)


# -----------------------
# Inicio del bot
# -----------------------

if __name__ == "__main__":
    print("Bot de moda iniciado 🩷✨")
    bot.infinity_polling()
