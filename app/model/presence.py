from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

class Presence:
    def __init__(self, id_presence=None):
        # ip='127.0.0.1'
        # port=27017
        # client=MongoClient(ip, port)
        client=pymongo.MongoClient("mongodb+srv://admin:adminkpm@cluster0.kpdlx.mongodb.net/presence?retryWrites=true&w=majority")
        dbName=client["presensidb"]
        self.colpresences=dbName["presence"]
        if id_presence:
            self.id_presence=id_presence
    
    def addPresence(self, id_event, attendace):
        presence_attr={ "id_event": id_event, "attendance": attendace}
        return self.colpresences.insert_one(presence_attr)
    
    def addPresenceMember(self, id_event, id_member):
        attendance=self.colpresences.find_one({"id_event": id_event})['attendance']
        if id_member in  attendance:
            return "Acara ini sudah dihadiri, silakan melihat pada menu Riwayat"
        attendance.append(id_member)
        set_member={"$set": {"attendance":attendance}}
        self.colpresences.update_one({"id_event": id_event}, set_member)
        return "Terimakasih sudah mengisi kehadiran"
    
    def getAllPresence(self):
        presences=self.colpresences.find()
        list_presence=[]
        for presence in presences:
            list_presence.append(presence)
        return list_presence
    
    def getDataPresence(self, id_event):
        return self.colpresences.find_one({"id_event": id_event})
    
    def deletePresence(self, id_event):
        return self.colpresences.delete_one({"id_event": id_event})


presence=Presence()
