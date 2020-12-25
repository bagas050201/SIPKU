from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

class Presence:
    def __init__(self, id_presence=None):
        ip='127.0.0.1'
        port=27017
        client=MongoClient(ip, port)
        dbName=client["presensidb"]
        self.colpresences=dbName["presence"]
        if id_presence:
            self.id_presence=id_presence
    
    def addPresence(self, id_presence, id_event, people):
        presence_attr={"id_presence": id_presence, "id_event": id_event, "people": people}
        return self.colpresences.insert_one(presence_attr)
    

    def getAllPresence(self):
        presence=self.colpresences.find()
        list_presence=[]
        for presence in presences:
            list_presence.append(presence)
        return list_presence
    