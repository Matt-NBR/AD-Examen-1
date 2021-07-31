#importar librerias
from facebook_scraper import get_posts
import json
import time
from pymongo import MongoClient

#Conectar con la instancia local de MongoDB
db_client = MongoClient('mongodb://localhost:27017')
#Seleccionar la base de datos creada
my_db = db_client.tokyo2021.facebook

i=1
#extraer posts de página seleccionada
for post in get_posts('Olympics', pages=100, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    #Separar toda la información del post
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['text']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}
        doc['post_url']=post['post_url']
        #Guardar la información en la base
        my_db.insert_one(doc)
        print("post saved")

    except Exception as e:    
        print("post not saved:" + str(e))
