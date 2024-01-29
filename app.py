from pymongo import MongoClient
import time

client = MongoClient("mongo:27017")
db = client["Tienda_videojuegos"]
collection = db["productos"]

while True:
    todos = list(collection.find())
    for todo in todos:
        print(todo)

    time.sleep(10)  # Espera 10 segundos antes de volver a consultar la base de datos
