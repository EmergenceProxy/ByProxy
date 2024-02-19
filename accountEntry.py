#Purpose: Simple class definition to store passwords in an encrypted format
import json
from cryptography.fernet import Fernet

class myAccountEntry:
    def __init__(self):
        self.accountHolder = ""
        self.email = ""
        self.username = ""
        self.password = ""
        #self.username = "aeDefault"
        #self.email = "aeDefault@def.org"
        #self.password = "aePass123"
        #self.accountHolder = "aeDefault.com"
        #print("myAccountEntry init")
#Getters
    def getAccountHolder(self):
        return self.accountHolder
    def getEmail(self):
        return self.email
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getDecPassword(self, accountKey):
        fernet = Fernet(accountKey)
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        decPW = fernet.decrypt(self.password)
        return decPW
#Setters
    def setAccountHolder(self, input):
        self.accountHolder = input
    def setEmail(self, input):
        self.email = input
    def setUsername(self, input):
        self.username = input
    def setPassword(self, accountKey, input):
        print("account key: ", accountKey)
        if len(accountKey) < 10:
            print("Need account key")
            return
        fernet = Fernet(accountKey.encode())
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        encPW = fernet.encrypt(input.encode())
        self.password = encPW.decode('utf-8')
#Utility
    def toString(self):
        #dataString = self.accountHolder+"::"+self.username+"::"+self.email+"::"+self.password
        jsonstr1 = json.dumps(self.__dict__)
        #dataStringy = json.loads(dataStringx)
        return jsonstr1
    def loadEntry(self, accountEntryText):
        if isinstance(accountEntryText, dict):
            #print("---is dict: ")
            if  len(accountEntryText["username"])>= 0:
                savedUN = accountEntryText["username"]
                #print("username string: ", savedUN)
            if  len(accountEntryText["email"]) >= 0:
                savedEmail = accountEntryText["email"]
                #print("Email string: ", savedEmail)
            if  len(accountEntryText["password"]) >= 0:
                savedPassword = accountEntryText["password"]
                #print("password string: ", savedPassword)
            if  len(accountEntryText["accountHolder"]) >= 0:
                savedActHolder= accountEntryText["accountHolder"]
                #print("accountHolder string: ", savedActHolder)
            
        if isinstance(accountEntryText, str):
            aetJson = json.loads(accountEntryText) 
            #print("account json string: ", aetJson)
            if  len(aetJson["username"])>= 0:
                savedUN = aetJson["username"]
                #print("username string: ", savedUN)
            if  len(aetJson["email"]) >= 0:
                savedEmail = aetJson["email"]
                #print("Email string: ", savedEmail)
            if  len(aetJson["password"]) >= 0:
                savedPassword = aetJson["password"]
                #print("password string: ", savedPassword)
            if  len(aetJson["accountHolder"]) >= 0:
                savedActHolder= aetJson["accountHolder"]
                #print("accountHolder string: ", savedActHolder)
                
        self.username = savedUN
        self.email = savedEmail
        self.password = savedPassword
        self.accountHolder = savedActHolder