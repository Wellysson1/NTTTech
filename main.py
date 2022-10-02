import json
import random
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

mydb = mysql.connector.connect(
    user="root", 
    password="Wc24031998",
    host="127.0.0.1"
    )
mycursor = mydb.cursor()
mycursor.execute("create database if not exists NTTechGrupo6;")
mycursor.execute("USE NTTechGrupo6;")
mycursor.execute("CREATE TABLE IF NOT EXISTS `nttechgrupo6`.`facts` (`Frase` VARCHAR(255) NOT NULL, UNIQUE INDEX `Frase_UNIQUE` (`Frase` ASC));;")
mycursor.execute("CREATE TABLE IF NOT EXISTS`nttechgrupo6`.`breed` (`Id_Breed` INT NOT NULL AUTO_INCREMENT, `Raca` VARCHAR(100) NOT NULL, PRIMARY KEY (`Id_Breed`), UNIQUE INDEX `Id_Breed_UNIQUE` (`Id_Breed` ASC) VISIBLE, UNIQUE INDEX `Raca_UNIQUE` (`Raca` ASC) VISIBLE);")

captura: list = []
lista_racas = []

for item in lista_racas:
    print(lista_racas)

app = FastAPI()

@app.get("/getRaca")
def insertBreed():
    mydb = mysql.connector.connect(
    user="root", 
    password="Wc24031998",
    host="127.0.0.1",
    database="nttechgrupo6"
    )
    mycursor = mydb.cursor()
    #mycursor.execute("INSERT IGNORE INTO breed (Raca) VALUES("Dog")")
    mycursor.commit()
    index = 0
    while (index < 173):
        response = requests.get("https://api.thedogapi.com/v1/breeds?&page=0")
        captura = json.loads(response.content)
        item = captura[index]['name']
        mycursor.execute("INSERT IGNORE INTO breed (Raca) VALUES(%s)", (item, ))
        mydb.commit()
        print(mycursor)
        index = index + 1        
    mydb.close()
    
    
@app.get("/getFacts")
def insertBreed():
    mydb = mysql.connector.connect(
    user="root", 
    password="Wc24031998",
    host="127.0.0.1",
    database="nttechgrupo6"
    )
    mycursor = mydb.cursor()
    index = 0
    while (index < 100):
        response = requests.get("https://dog-api.kinduff.com/api/facts")
        captura = json.loads(response.content)
        item = captura['facts'][0]
        mycursor.execute("INSERT IGNORE INTO facts (Frase) VALUES(%s)", (item, ))
        mydb.commit()
        print(mycursor)
        index = index + 1        
    mydb.close()
              


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



