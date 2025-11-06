import json
import os

class AnalizarVoz():
    def __init__(self, bot, groq):
        self.bot = bot
        self.groq = groq

    def load_fashion_data(self):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, "fashion_dataset.json")
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error al cargar el dataset: {str(e)}")
            return None

    def get_groq_fashion_response(self, user_message: str):

        fashion_data = self.load_fashion_data()

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
    6. No inventes marcas ni precios si no están en el dataset."""

            chat_completion = self.groq.chat.completions.create(
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
    
    def transcribe_voice_with_groq(self, message): #message es el mensaje que manda el usuario
        try:
            file_info = self.bot.get_file(message.voice.file_id)
            print(f"🎙️ Archivo recibido: {file_info.file_path}")
            downloaded_file = self.bot.download_file(file_info.file_path)

            temp_file = "temp_voice.ogg"
            
            with open(temp_file, "wb") as f:
                f.write(downloaded_file)

            print("📤 Enviando a Whisper para transcripción...")
            with open(temp_file, "rb") as file:
                transcription = self.groq.audio.transcriptions.create(
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