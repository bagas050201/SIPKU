from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo


class Event:
    def __init__(self, id_event=None):
        # ip='127.0.0.1'
        # port=27017
        # client=MongoClient(ip, port)
        client=pymongo.MongoClient("mongodb+srv://admin:adminkpm@cluster0.kpdlx.mongodb.net/event?retryWrites=true&w=majority")
        dbName=client["presensidb"]
        self.colevents=dbName["event"]
        if id_event:
            self.id_event=id_event
    
    def addEvent(self,title, description, poster, date, time, status):
        event_attr={ "title": title, "description": description, "poster": poster, "date": date, "time": time, "status": status}
        return self.colevents.insert_one(event_attr)
    
    def getTitle(self):
        return self.colevents.find_one({"_id": self.id_event})['title']
    
    def getDate(self):
        return self.colevents.find_one({"_id": self.id_event})['date']
    
    def updateEvent(self, id_event,title, description, date, time, status):
        update_event={"$set": {"title": title, "description": description, "date": date, "time": time, "status": status}}
        return self.colevents.update_one({"_id":ObjectId(id_event)}, update_event)
    
    def deleteEvent(self, id_event):
        return self.colevents.delete_one({"_id": ObjectId(id_event)})  
    
    def getAllEvents(self):
        events=self.colevents.find()
        list_event=[]
        for event in events:
            event['_id']=str(event['_id'])
            list_event.append(event)
        return list_event
    
    def getId(self, title, desc, date, time):
        return self.colevents.find_one({"title": title, "description": desc, "date": date, "time": time})['_id']


event= Event()
