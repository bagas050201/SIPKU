from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo


class Log:
    def __init__(self, id_log=None):
        # ip='127.0.0.1'
        # port=27017
        # client=MongoClient(ip, port)
        client=pymongo.MongoClient("mongodb+srv://admin:adminkpm@cluster0.kpdlx.mongodb.net/log?retryWrites=true&w=majority")
        dbName=client["presensidb"]
        self.collogs=dbName["log"]
        if id_log:
            self.id_log=id_log
    
    def addLog(self, activity):
        log_attr={"activity": activity}
        return self.collogs.insert_one(log_attr)

