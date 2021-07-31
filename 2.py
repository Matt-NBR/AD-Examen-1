#Importando las librerias
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#API keys
key = "PoxcB6o7AByoSia0BknF2E3BX"
secret = "JuOThJB0kkyBcLPY4gGco4FgpYVQD03TCXwcFM5s8VDsrvSIRF"
atoken = "1415856712490307584-yLiFWBRSDvo7pl8k1DPfobjQiSIbC8"
asecret = "idp4j4MrP212yRQRZySE1jh0HYy51wNxyJsKC8ylglTfs"

#Conexion al servidor de couchdb
server = couchdb.Server('http://mateo:couchdb@localhost:5984/')

#creacion de una base para tweets segun palabra clave
try:
    db2 = server.create('tokyo2021-track')
except:
    db2 = server['tokyo2021-track']
    
class listener(StreamListener):
    #Funcion para guardar tweets como documentos en la base
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db2.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)

#pasando las keys de autorizacion al stream de twitter        
auth = OAuthHandler(key, secret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#Consultar el stream segun palabras clave
twitterStream.filter(track=['tokyo2021', 'olympics'])
