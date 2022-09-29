import json
import random
import requests
from fastapi import FastAPI
from pydantic import BaseModel


MODE_ENCRYPT = 1
app = FastAPI()
alphabet = 'abcdefghijklmnopqrstuvwyz'
    
class Itemm(BaseModel):
    frase : str
    key : int

@app.get("/getCifra")
def codifica():
    response = requests.get("http://dog-api.kinduff.com/api/facts")
    captura = json.loads(response.content)
    frase = captura['facts'][0]
    key = random.randrange(1,24)
    class jsson():
        def __init__(self, frase):
            self.ciphered = frase
            self.key = key
            data = json.dumps(json.__dict__)
            ciphered = codifica(frase, key, MODE_ENCRYPT)
    new_data = ''
    for c in frase:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return {"frase": new_data, "Chave": key}

@app.post("/resolveCifra")
def decodifica(itemm:Itemm):
    frase, key = itemm
    frase = frase[1]
    key = key[1]
    new_data = ""
    for c in frase:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index - int(key)
            new_index = new_index % len(alphabet) %27
            new_data += alphabet[new_index:new_index+1]
    return {"Frase": new_data, "Chave utilizada": key}



