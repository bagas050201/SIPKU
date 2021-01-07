from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo
from .presence import Presence
from .event import Event

class Member:
    def __init__(self, id_member=None):
        # ip='127.0.0.1'
        # port=27017
        # client=MongoClient(ip, port)
        client=pymongo.MongoClient("mongodb+srv://admin:adminkpm@cluster0.kpdlx.mongodb.net/member?retryWrites=true&w=majority")
        dbName=client["presensidb"]
        self.colmembers=dbName["member"]
        if id_member:
            self.id_member=id_member
    
    def getIdMember(self):
        return self.id_member
    
    def addMember(self,id_member, fullname, study, gen, password, photo):
        member_attr={"id_member": id_member, "fullname": fullname, "study": study, "gen": gen, "password": password, "photo": photo}
        return self.colmembers.insert_one(member_attr)
    
    def updateMember(self, fullname, study, gen):
        update_member={"$set": {"fullname": fullname, "study": study, "gen": gen}}
        return self.colmembers.update_one({"id_member":self.id_member}, update_member)
    

    def getFullname(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})['fullname']
    
    def setFullname(self, id_member, fullname):
        set_fullname={"$set": {"fullname":fullname}}
        return self.colmembers.update_one({"id_member":id_member}, set_fullname)
    
    def getPhoto(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})['photo']
    
    def setPhoto(self, id_member, photo):
        set_photo={"$set": {"photo":photo}}
        return self.colmembers.update_one({"id_member":id_member}, set_photo)
    
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
    
    def deleteMember(self, id_member):
        return self.colmembers.delete_one({"id_member": id_member})
    
    def getDataMember(self, id_member):
        return self.colmembers.find_one({"id_member": id_member})

    def getDataPresenceMember(self, id_member):
        kehadiran=Presence().getAllPresence()
        temp_data={}
        data_kehadiran=[]
    
        for data in kehadiran  :
            temp_data['title']= Event(ObjectId(data['id_event'])).getTitle()
            temp_data['date']=Event(ObjectId(data['id_event'])).getDate()
            if str(id_member) in data['attendance']:
                temp_data['status']='Hadir'
            else:
                temp_data['status']="Tidak Hadir"
            data_kehadiran.append(temp_data)
            temp_data={}
        return data_kehadiran

    def getAllMembers(self):
        members=self.colmembers.find()
        list_member=[]
        for member in members:
            list_member.append(member)
        return list_member
    
    def getAllId(self):
        members=self.colmembers.find()
        list_id=[]
        for member in members:
            list_id.append(member['id_member'])
        return list_id
    
    def getAllPassword(self):
        members=self.colmembers.find()
        list_pass=[]
        for member in members:
            list_pass.append(member['password'])
        return list_pass
    

