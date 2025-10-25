#Agregue esto porque Python no encontraba las otras carpetas-----------------------------

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
#-------------------------------------------------------------------------------------

import telebot
import random
from ChatBot.Core import responder, mostrar_menu, usuarios_estado
from Modelo.Usuario import Usuario
#from RespuestasGroq.Predefinidas import ResponderDataset
from transformers import pipeline

from Analizador.AnalizarSentimiento import AnalizarSentimiento


# ⚙️ Configuración del token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8336358155:AAHkwdN4i6zbW-5af3Gp7LAZwYMjqUIaEz4")

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

@bot.message_handler(commands=['analizar'])  
def  analizar_mensaje(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Escribi el mensaje que quieras analizar")
    bot.register_next_step_handler(message, analizar_texto) #Esta funcion captura el mensaje que envia el usuario inmediatamente despues del comando /analisis y lo envia a la funcion analizar_texto

def analizar_texto(message):
    user_id = message.from_user.id
    texto = message.text.strip()

    resultado = AnalizarSentimiento().analizar_sentimiento(texto) #Analizo el mensaje que manda el usuario llamando al metodo analizar_sentimiento

    bot.send_message(user_id, f"El resultado de tu analisis: {resultado}") #El bot le manda al usuario el analisis de sentimiento de su mensaje 

#    ds = ResponderDataset().cargar_dataset()
#    respuesta = ResponderDataset().buscar_en_dataset(texto,ds)
#    if respuesta:
#        bot.reply_to(message, respuesta)
#    else:
#        bot.reply_to(message, "No tengo esta respuesta")


@bot.message_handler(func=lambda m: True)
def menu(message):
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
