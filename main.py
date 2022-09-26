from ast import Num
from calendar import c
from numbers import Number
import numbers
from string import ascii_lowercase
from typing import Union
import json, requests
from unicodedata import numeric
from urllib import response
from fastapi import FastAPI
import random
from pydantic import BaseModel
from json import loads


response = requests.get("http://dog-api.kinduff.com/api/facts")
captura = json.loads(response.text)
frase = captura['facts'][0]
#print(json_data[0]['res'][0])

MODE_ENCRYPT = 1
MODE_DECRYPT = 0
alphabet = 'abcdefghijklmnopqrstuvwyz'

app = FastAPI()
@app.get("/getCifra")
def codifica(data, key, mode):
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else print("Erro")
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return {"Frase": new_data, "Chave": key}

key = random.randrange(1,24)
original = frase
ciphered = codifica(original, key, MODE_ENCRYPT)
class json():
    def __init__(self, frase, key):
        self.ciphered = frase
        self.key = key
        data = json.dumps(json.__dict__)
    
print('Encriptada:', ciphered)

@app.post("/resolveCifra")
def decodifica(frase, key):
    new_data = ''
    for c in frase:
        index = ((ord(c) - ord('a')) + 26 - key) %26
        new_data += alphabet[index]
    return {"Mensagem Decifrada": new_data}


    









