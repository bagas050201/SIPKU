from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

class Event:
    def __init__(self, id_event=None):
        ip='127.0.0.1'
        port=27017
        client=MongoClient(ip, port)
        dbName=client["presensidb"]
        self.colevents=dbName["event"]
        if id_event:
            self.id_event=id_event
    
    def addEvent(self, id_event, title, description, poster, date, time, status, presence):
        event_attr={"id_event": id_event, "title": title, "description": description, "poster": poster, "date": date, "time": time, "status": status, "presence": presence}
        return self.colevents.insert_one(event_attr)
    
    def updateEvent(self, id_event,title, description, poster, date, time, status, presence):
        update_event={"$set": {"title": title, "description": description, "poster": poster, "date": date, "time": time, "status": status, "presence": presence}}
        return self.colevents.update_one({"id_event":id_event}, update_event)
    
    
    def getAllEvents(self):
        events=self.colevents.find()
        list_event=[]
        for event in events:
            list_event.append(event)
        return list_event
    
    
