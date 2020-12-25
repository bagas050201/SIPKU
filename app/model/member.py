from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

class Member:
    def __init__(self, id_member=None):
        ip='127.0.0.1'
        port=27017
        client=MongoClient(ip, port)
        dbName=client["presensidb"]
        self.colmembers=dbName["member"]
        if id_member:
            self.id_member=id_member
    
    def addMember(self,id_member, fullname, study, gen, password):
        member_attr={"id_member": id_member, "fullname": fullname, "study": study, "gen": gen, "password": password}
        return self.colmembers.insert_one(member_attr)
    
    def updateMember(self, id_member, fullname, study, gen, password):
        update_member={"$set": {"fullname": fullname, "study": study, "gen": gen, "password": password}}
        return self.colmembers.update_one({"id_member":id_member}, update_member)
    
    def getFullname(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})['fullname']
    
    def setFullname(self, id_member, fullname):
        set_fullname={"$set": {"fullname":fullname}}
        return self.colmembers.update_one({"id_member":id_member}, set_fullname)
    
    def getStudy(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})['study']
    
    def setStudy(self, id_member, study):
        set_study={"$set": {"study":study}}
        return self.colmembers.update_one({"id_member":id_member}, set_study)
    
    def getGen(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})['gen']
    
    def setGen(self, id_member, gen):
        set_gen={"$set": {"gen":gen}}
        return self.colmembers.update_one({"id_member":id_member}, set_gen)
    
    def getPassword(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})['password']
    
    def setPassword(self, id_member, password):
        set_password={"$set": {"password":password}}
        return self.colmembers.update_one({"id_member":id_member}, set_password)
    
    def getDataMember(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})
        
    def getAllMembers(self):
        members=self.colmembers.find()
        list_member=[]
        for member in members:
            list_member.append(member)
        return list_member
    

# member= Member()
# member.addMember(12345, "Alfachri", "Ilkom", 2020, "sesuatu") 
