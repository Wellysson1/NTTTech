from ast import Await, Num
from itertools import count
from numbers import Number
import numbers
from string import ascii_lowercase
from typing import Union
import json
from unicodedata import numeric
from urllib import response
from fastapi import FastAPI
import random
from pydantic import BaseModel
from json import loads
from fastapi.responses import JSONResponse
import requests


response = requests.get("http://dog-api.kinduff.com/api/facts")
captura = json.loads(response.text)
frase = captura['facts'][0]
#print(json_data[0]['res'][0])

app = FastAPI()
MODE_ENCRYPT = 1
alphabet = 'abcdefghijklmnopqrstuvwyz'
key = random.randrange(1,24)

class Item(BaseModel):
    frase = str

@app.get("/getCifra")
def codifica(frase, key, mode):
    new_data = ''
    for c in frase:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else print("Erro")
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return {"Frase": new_data, "chave": key}


original = frase
ciphered = codifica(frase, key, MODE_ENCRYPT)
class json():
    def __init__(self, frase, key):
        self.ciphered = frase
        self.key = key
        data = json.dumps(json.__dict__)
    
print('Encriptada:', ciphered) 



@app.post("/resolveCifra")
def decodifica(frase, key):
    response = requests.get("http://127.0.0.1:8000/resolveCifra")
    captura = json.loads(response.text)
    frase = captura['Frase'][0]
    capturakey = json.loads(response.text)
    key = capturakey['Key'][0]
    new_data = ''
    for c in frase:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index - int(key)
            new_index = new_index % len(alphabet) %27
            new_data += alphabet[new_index:new_index+1]
    return {"Mensagem Decifrada": new_data}
    



    









