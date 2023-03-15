from fastapi import FastAPI
import string

app = FastAPI()

@app.get('/reverse-int/{numero}')
def inverter_digitos(numero: int):
    negativo = False
    if numero < 0:
        negativo = True
        numero *= -1
    numero_invertido = int(str(numero)[::-1])

    if negativo:
        numero_invertido *= -1
    return {'numero invertido': numero_invertido}

@app.post('/words-length/')
def comprimento(frase: str):
    for palavra in frase:
        if palavra in string.punctuation:
            frase = frase.replace(palavra, '')
    
    palavras = frase.split()
    comprimento_medio = sum(len(palavra) for palavra in palavras) / len(palavras)

    return {'comprimento médio': comprimento_medio}

@app.post('/words/')
def palavras(frase1: str, frase2: str):
    for palavra in frase1:
        if palavra in string.punctuation:
            frase1 = frase1.replace(palavra, '')
    for palavra in frase2:
        if palavra in string.punctuation:
            frase2 = frase2.replace(palavra, '')

    palavras1 = set(frase1.split())
    palavras2 = set(frase2.split())

    palavras_iguais = palavras1.intersection(palavras2)
    palavreas_diferentes = palavras1.symmetric_difference(palavras2)
    
    return {'palavras em comum':list(palavras_iguais),
            'palavras diferentes': list(palavreas_diferentes)}