import base64
import json
from AnalisisVoz.AnalizarVoz import AnalizarVoz

class AnalizarImagen(AnalizarVoz):

    def __init__(self, bot, groq):
        super().__init__(bot, groq)  # Llamamos al constructor del padre
        
    def analizar_imagen(self, message):

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


            file_info = self.bot.get_file(message.photo[-1].file_id)
            downloaded_file = self.bot.download_file(file_info.file_path)
            image_base64 = base64.b64encode(downloaded_file).decode("utf-8")

            self.bot.reply_to(message, "💌Analizando tu imagen...⏱ ")

            response = self.groq.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Analiza esta imagen de ropa y aplica el prompt anterior."},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
                        ]
                    }
                ],
            )

            resultado = response.choices[0].message.content
            self.bot.reply_to(message, f"💌 <b>Análisis de la imagen:</b>\n{resultado}", parse_mode="HTML")

            return  

        except Exception as e:
            self.bot.reply_to(message, f"⚠️ Error al procesar la imagen:\n{str(e)}")
            return  
