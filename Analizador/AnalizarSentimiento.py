from transformers import pipeline

class AnalizarSentimiento:
    def __init__(self):
        pass
    
    def analizar_sentimiento(self, frase):
        
        analizador_sentimiento = pipeline('sentiment-analysis', model = 'pysentimiento/robertuito-sentiment-analysis')
        
        resultado = analizador_sentimiento(frase)[0]

        sentimiento = resultado['label']  #traigo la etiqueta label y score
        confianza = resultado['score']

        if sentimiento.lower() == 'pos':
            sentimiento = 'Sentimiento positivo'
            emoji = ':)'
        elif sentimiento.lower() == 'neu':
            sentimiento = 'Sentimiento neutro'
            emoji = ':|'
        elif sentimiento.lower() == 'neg':
            sentimiento = 'Sentimiento negativo'
            emoji = ':('
        else:
            emoji = 'H'

        answer = f'{sentimiento.upper()} {emoji}\n Confianza: {confianza:2%}'

        return answer
    