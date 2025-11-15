# Chatbot de Moda 

## Descripción del proyecto
El **Chatbot de Moda** es un asistente virtual diseñado para ayudarte a elegir tus outfits, combinar colores, analizar tu estado de ánimo ¡y mucho más!  
A través de un menú interactivo, el chatbot te guía para crear combinaciones únicas, obtener recomendaciones según el clima o incluso analizar imágenes y audios.  
Su objetivo es hacer que vestirse sea una experiencia divertida, sencilla, sin necesidad de perder mucho tiempo  y sobre todo que sea ¡muy fashionista! ✨

---

## Ejecución del chatbot

Para ejecutar el chatbot, abrí tu consola o terminal en la carpeta del proyecto y escribí el siguiente comando:

```bash
python -m TeleBot.Handler
```

---

## Comando '/start'

Para iniciar la conversación con el chatbot, escribí en el chat de Telegram: '/start'


Al hacerlo, recibirás un mensaje de bienvenida como:

>  “¡Hola! Soy tu asistente de moda ✨. Estoy acá para ayudarte a combinar tus outfits, elegir looks y mantener tu estilo al día.”

Luego, un segundo mensaje te preguntará cómo querés continuar y mostrará las **6 opciones del menú principal** para empezar a interactuar.


## Menú principal

Una vez que el chatbot está en funcionamiento, te mostrará el **menú con las 6 opciones principales:**

---

### 1️⃣ Sugerir outfit del día

El chatbot genera un **outfit aleatorio** para el día.  
Si volvés a elegir la opción 1, te mostrará una nueva sugerencia distinta.

**Ejemplo:**  
> “Para hoy te recomiendo un jean celeste, una blusa blanca y zapatillas beige. ¡Un look casual pero con estilo!”

---

### 2️⃣ Ver combinaciones de colores

Podés escribir un color (por ejemplo, “rosa”) y el chatbot te sugerirá combinaciones posibles con ese tono.

 **Ejemplo:**  
> “El color rosa combina muy bien con una chaqueta blanca y zapatos rosas.”

Después, vuelve a mostrarte el menú para seguir explorando.

---

### 3️⃣ Armar outfit con tu guardarropa

Contale al chatbot qué prendas querés usar o qué tenés en mente, y él te ayudará a **completar el look.**

**Ejemplo:**  
> “Tengo un pantalón blanco y una remera marrón.”  
 **Respuesta:** “Perfecto, con eso podrías combinar zapatillas blancas o un blazer gris claro. ¿Querés agregar un accesorio?”

Si respondés que sí, te sugerirá opciones (por ejemplo, una pulsera plateada o un bolso claro). 
Si respondés que no, el chatbot sigue y te muestra el menu nuevamente por si queres seguir interactuando con él.
---

### 4️⃣ Sugerir outfit según el clima

Indicá el clima del día (por ejemplo, “frío”, “lluvia”, “soleado”) y el chatbot te recomendará un conjunto acorde.

 **Ejemplo:**  
> “Hoy está frío, te recomiendo usar un abrigo gris, una bufanda rosa y unas botas negras.”

---

### 5️⃣ Analizar sentimiento de un texto

En esta opción podés escribir un texto libre (por ejemplo, cómo te sentís o una frase).  
El chatbot lo analiza y te indica si el **sentimiento** es **positivo**, **negativo** o **neutral**, junto con un **porcentaje de certeza.**

**Ejemplo:**  
> “Hoy me siento súper feliz.”  
 **Respuesta:** “Tu mensaje tiene un sentimiento positivo! espero que hoy tengas un lindo dia”

---

### 6️⃣ Salir

Finaliza la sesión con un mensaje simpático:

 **Ejemplo:**  
> “Bye, ¡que tengas un día fashionista!”

---

## Comando especial: `/charlar`

Podés usar el comando `/charlar` para tener una **conversación libre sobre moda** con el chatbot.  
En esta sección podés preguntarle **consejos, tendencias, combinaciones**, o simplemente charlar sobre **outfits y estilo personal.**

 **Importante:**  
El chatbot está especializado en **temas de moda**, por lo que no responderá preguntas fuera de ese ámbito (por ejemplo, sobre cocina o deportes).

Podés seguir conversando todo lo que quieras, y para salir de esta sección solo tenés que escribir `/salir`.  
Hasta que no uses ese comando, la conversación continuará en el **modo charla de moda.** 

---

## Funcionalidad extra: Envío de audios

El chatbot también acepta **mensajes de voz.**  
Por ejemplo, podés enviar un audio diciendo:

> “Quiero un outfit para una cena con amigos esta noche.”

El chatbot **transcribe el audio** y genera una **respuesta personalizada**, usando la **API de Groq** para el procesamiento de voz.

---

## Funcionalidad extra: Análisis de imágenes

Podés **adjuntar una imagen** (por ejemplo, una foto de tu outfit o prenda), y el chatbot la **analizará y describirá lo que ve.**

👀 **Ejemplo:**  
> “Veo una falda negra, una blusa blanca y un bolso beige. ¡Un look elegante y clásico!”

---

## Tecnologías utilizadas

- **Python**   
- **TeleBot / PyTelegramBotAPI**  
- **API Groq** (para reconocimiento de voz)  
- **Modelos de análisis de imagen y sentimiento**  
- **Integraciones personalizadas para generar respuestas dinámicas**

---

## 💡 Consejos de uso

- Respondé con los **números del menú (1 a 6)** para moverte entre las opciones.  
- En la sección de charla (`/charlar`), podés expresarte libremente sobre **moda.**  
- Si el chatbot no entiende un comando, te mostrará nuevamente el menú principal.  
- ¡Probá distintas combinaciones y descubrí nuevos estilos! ✨


---

## Autoras

**Desarrollado por:** 💻 *Las Hechiseras del Código* ✨  
👩‍💻 **Karen Mejía**  
👩‍💻 **Sandra Quispe**  
👩‍💻 **Heydi Titirico**

Proyecto realizado con dedicación y estilo:🪄  
> *“La moda se trata de expresar quién sos sin tener que decir una palabra.”* 👗

---