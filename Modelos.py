from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://demoya739:13579@cluster0.kmkd4tv.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

# definimos el método de conexión

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["Proyecto"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db