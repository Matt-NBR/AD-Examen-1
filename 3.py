#importar librerias
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import bson
from bson.raw_bson import RawBSONDocument

#Conectar con la instancia local de MongoDB
db_client = MongoClient('mongodb://localhost:27017')
#Seleccionar la base de datos creada
my_db = db_client.tokyo2021.web

#Funciones para encontrar subcadenas    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))   

#Especificando el sitio que se va a usar
response = requests.get("https://edition.cnn.com/world/live-news/tokyo-2020-olympics-07-30-21-spt/index.html")
#creando el objeto de beautiful soup
soup = BeautifulSoup(response.content, "lxml")

#se extrae los titulos luego de analizar el patrón de repetición
titles = soup.find_all("h2", class_="sc-gxMtzJ RIfoo")

#se crea lista para información extraída
extracted = []

#Se recorre todos los titulos encontrados
for element in titles:
    element=str(element)
    #Se limpia la información quitando las etiquetas html
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #se añade la información a la lista
    extracted.append(limpio)
        
#Guardar información de la lista en el cliente de MongoDB
for post in extracted:
    #Imprimir el post a guardar
    print(post)
    #transformar el post a json
    jsonDoc = {"Title": post}
    try:
        #Guardar el post
        my_db.insert_one(jsonDoc)
        print("post saved")
    except Exception as e:
        print("post was not saved" + str(e))
