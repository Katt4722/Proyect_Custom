# 🤖 Proyecto de Análisis de Sentimientos con Transformers

Este proyecto utiliza la biblioteca **Transformers** de Hugging Face para realizar análisis de sentimientos en texto en español. Es perfecto para estudiantes que están comenzando en el mundo del procesamiento de lenguaje natural (NLP) y la inteligencia artificial.

## 📋 Tabla de Contenidos
- [¿Qué hace este proyecto?](#-qué-hace-este-proyecto)
- [Requisitos previos](#-requisitos-previos)
- [Instalación paso a paso](#-instalación-paso-a-paso)
- [Cómo ejecutar el proyecto](#-cómo-ejecutar-el-proyecto)
- [¿Cómo funciona el código?](#-cómo-funciona-el-código)
- [Personalización](#-personalización)
- [Posibles errores y soluciones](#-posibles-errores-y-soluciones)
- [Referencias](#-referencias)

---

## 🎯 ¿Qué hace este proyecto?

Este proyecto analiza el **sentimiento** (emociones) de frases en español y te dice si son:
- **😊 Muy positivas** (5 estrellas)
- **🙂 Positivas** (4 estrellas)  
- **😐 Neutrales** (3 estrellas)
- **😟 Negativas** (2 estrellas)
- **😠 Muy negativas** (1 estrella)

**Ejemplo de uso:**
```
Frase: "¡Me encantó este curso, aprendí muchísimo!"
-> Sentimiento Detectado: 5 STARS 😊 (Confianza: 89.45%)
```

---

## 🔧 Requisitos previos

Antes de comenzar, necesitas tener instalado:

### 1. Python 3.8 o superior
- **Windows**: Descarga desde [python.org](https://www.python.org/downloads/)
- **Verificar instalación**: Abre la terminal y ejecuta:
  ```bash
  python --version
  ```
  Debería mostrar algo como: `Python 3.11.0`

### 2. Git (opcional pero recomendado)
- **Windows**: Descarga desde [git-scm.com](https://git-scm.com/)
- Esto te permitirá clonar el proyecto fácilmente

### 3. Un editor de código
- **Recomendado**: [Visual Studio Code](https://code.visualstudio.com/)
- **Alternativas**: PyCharm, Sublime Text, o cualquier editor de texto

---

## 🚀 Instalación paso a paso

### Paso 1: Descargar el proyecto

**Opción A: Con Git (recomendado)**
```bash
git clone <URL_DEL_REPOSITORIO>
cd Transformers
```

**Opción B: Descarga manual**
1. Descarga el proyecto como ZIP
2. Extrae los archivos en una carpeta (ej: `D:\SIC\Transformers`)
3. Abre la terminal en esa carpeta

### Paso 2: Crear el entorno virtual

Un **entorno virtual** es como una "caja separada" donde instalamos las librerías específicas de nuestro proyecto, sin afectar otras instalaciones de Python.

```bash
# Crear el entorno virtual
python -m venv entorno-transformers

# Verificar que se creó la carpeta
ls entorno-transformers  # En Linux/Mac
dir entorno-transformers  # En Windows CMD
```

### Paso 3: Activar el entorno virtual

**En Windows (Git Bash/MINGW64):**
```bash
source entorno-transformers/Scripts/activate
```

**En Windows (CMD):**
```cmd
entorno-transformers\Scripts\activate.bat
```

**En Windows (PowerShell):**
```powershell
entorno-transformers\Scripts\Activate.ps1
```

**En Linux/Mac:**
```bash
source entorno-transformers/bin/activate
```

✅ **¿Cómo saber si está activado?**
Tu terminal debería mostrar `(entorno-transformers)` al inicio de la línea:
```bash
(entorno-transformers) usuario@computadora:/ruta/del/proyecto$
```

### Paso 4: Instalar las dependencias

Ahora instalamos todas las librerías necesarias:

```bash
# Actualizar pip (recomendado)
python -m pip install --upgrade pip

# Instalar todas las dependencias del proyecto
pip install -r requirements.txt
```

⏰ **¡Paciencia!** Este proceso puede tomar varios minutos (5-15 min) ya que descarga librerías grandes como PyTorch y Transformers.

### Paso 5: Verificar la instalación

```bash
# Verificar que las librerías principales están instaladas
python -c "import transformers; print('✅ Transformers instalado correctamente')"
python -c "import torch; print('✅ PyTorch instalado correctamente')"
```

---

## ▶️ Cómo ejecutar el proyecto

### 1. Asegúrate de que el entorno virtual esté activado
```bash
# Deberías ver (entorno-transformers) en tu terminal
source entorno-transformers/Scripts/activate  # Si no está activado
```

### 2. Ejecutar el programa principal
```bash
python main.py
```

### 3. ¡Espera los resultados!

La primera vez tardará un poco más porque debe descargar el modelo de IA desde internet. Verás algo así:

```
Cargando el modelo de análisis de sentimiento...
¡Modelo cargado con éxito! ✅

Analizando frases...

Frase: '¡Me encantó este curso, aprendí muchísimo!'
  -> Sentimiento Detectado: 5 STARS 😊 (Confianza: 89.45%)

Frase: 'El servicio al cliente fue bastante lento y poco útil.'
  -> Sentimiento Detectado: 2 STARS 😟 (Confianza: 76.82%)

... (más resultados)
```

---

## 🧠 ¿Cómo funciona el código?

### Estructura del archivo `main.py`:

```python
# 1. Importar la biblioteca
from transformers import pipeline

# 2. Crear el analizador de sentimientos
analizador_sentimiento = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# 3. Preparar frases para analizar
frases_para_analizar = [
    "¡Me encantó este curso, aprendí muchísimo!",
    # ... más frases
]

# 4. Analizar cada frase
resultados = analizador_sentimiento(frases_para_analizar)

# 5. Mostrar resultados con emojis
for frase, resultado in zip(frases_para_analizar, resultados):
    sentimiento = resultado['label']    # Ej: '5 stars'
    confianza = resultado['score']      # Ej: 0.8945 (89.45%)
    print(f"Frase: '{frase}'")
    print(f"Sentimiento: {sentimiento} (Confianza: {confianza:.2%})")
```

### Conceptos clave:

- **Pipeline**: Una "tubería" que procesa texto automáticamente
- **Modelo BERT**: Un modelo de IA entrenado para entender texto
- **Multilingüe**: Funciona con varios idiomas, incluyendo español
- **Confianza**: Qué tan seguro está el modelo de su predicción (0-100%)

---

## 🎨 Personalización

### Cambiar las frases a analizar

Edita la lista `frases_para_analizar` en `main.py`:

```python
frases_para_analizar = [
    "Tu primera frase aquí",
    "Tu segunda frase aquí",
    "¡Puedes agregar todas las que quieras!",
    # Agregar más frases...
]
```

### Probar con frases interactivas

Puedes modificar el código para que pida frases al usuario:

```python
# Agregar al final de main.py
print("\n" + "="*50)
print("¡Ahora prueba con tus propias frases!")
print("(Escribe 'salir' para terminar)")

while True:
    frase_usuario = input("\nEscribe una frase: ")
    if frase_usuario.lower() == 'salir':
        print("¡Hasta luego! 👋")
        break
    
    resultado = analizador_sentimiento([frase_usuario])[0]
    sentimiento = resultado['label']
    confianza = resultado['score']
    
    # Mapear emoji (mismo código que antes)
    emoji = "❓"
    if "star" in sentimiento:
        if sentimiento == '5 stars':
            emoji = "😊"
        elif sentimiento == '4 stars':
            emoji = "🙂"
        # ... etc
    
    print(f"  -> {sentimiento.upper()} {emoji} (Confianza: {confianza:.2%})")
```

### Usar otros modelos

Puedes probar otros modelos cambiando esta línea:

```python
# Modelo actual (multilingüe)
model="nlptown/bert-base-multilingual-uncased-sentiment"

# Alternativa 1: Modelo más simple
# model="cardiffnlp/twitter-roberta-base-sentiment-latest"

# Alternativa 2: Modelo específico para español
# model="finiteautomata/beto-sentiment-analysis"
```

---

## ❌ Posibles errores y soluciones

### Error: "No module named 'transformers'"
**Problema**: El entorno virtual no está activado o las librerías no están instaladas.

**Solución**:
```bash
# 1. Activar entorno virtual
source entorno-transformers/Scripts/activate

# 2. Reinstalar librerías
pip install -r requirements.txt
```

### Error: "torch" not found o similar
**Problema**: PyTorch no se instaló correctamente.

**Solución**:
```bash
# Instalar PyTorch manualmente
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Error de conexión a internet
**Problema**: No puede descargar el modelo.

**Solución**:
- Verifica tu conexión a internet
- Intenta ejecutar el programa más tarde
- El modelo se descarga una sola vez y se guarda localmente

### Error: "Permission denied" o permisos
**Problema**: No tienes permisos para instalar en esa carpeta.

**Solución**:
```bash
# Opción 1: Usar --user
pip install --user -r requirements.txt

# Opción 2: Ejecutar como administrador (Windows)
# Clic derecho en terminal > "Ejecutar como administrador"
```

### El programa funciona muy lento
**Solución**:
- Es normal la primera vez (descarga el modelo)
- Las siguientes ejecuciones serán más rápidas
- Reduce el número de frases si es necesario

---

## 📚 Referencias

### Documentación oficial:
- [🤗 Transformers Library](https://huggingface.co/docs/transformers)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Hugging Face Models](https://huggingface.co/models)

### Modelo utilizado:
- [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)

### Conceptos para aprender más:
- **BERT**: Bidirectional Encoder Representations from Transformers
- **NLP**: Natural Language Processing (Procesamiento de Lenguaje Natural)
- **Transfer Learning**: Usar modelos pre-entrenados
- **Sentiment Analysis**: Análisis de sentimientos

---

## 🤝 Contribuir

¿Tienes ideas para mejorar el proyecto? ¡Genial!

1. Haz un fork del repositorio
2. Crea una nueva rama: `git checkout -b mi-mejora`
3. Realiza tus cambios
4. Haz commit: `git commit -m "Agrego nueva funcionalidad"`
5. Sube los cambios: `git push origin mi-mejora`
6. Crea un Pull Request

---

## 📄 Licencia

Este proyecto es de uso educativo. Siéntete libre de usarlo y modificarlo para aprender.

---

## 💡 Próximos pasos para los que no tienen ni plata ni miedo 

Una vez que domines este proyecto, puedes:
1. **Analizar archivos CSV** con miles de comentarios
2. **Crear una interfaz web** con Flask/Streamlit  
3. **Entrenar tu propio modelo** con datos específicos
4. **Analizar otros idiomas** cambiando el modelo
5. **Integrar con APIs** de Twitter, Reddit, etc.

¡Happy coding! 🚀

---

*Creado con ❤️ para estudiantes de IA y Python del SIC*
