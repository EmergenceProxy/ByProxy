#Purpose: Simple class definition to store passwords in an encrypted format
#add bill manager.
from cryptography.fernet import Fernet
from datetime import datetime
import json
import os
from accountEntry import myAccountEntry as accountEntry



class myAccountBook:
    def __init__(myactbook):
        #myactbook.name = name
        #myactbook.age = age
        myactbook.accountKey = ""
        myactbook.accountEmail = ""
        myactbook.sessionKey = ""
        myactbook.sessionFile = ""#savKey2023-09-24_19.21.58.475349.bean.txts
        myactbook.accountsList = []#list of dictionaries instead of accountEntry's to stay serializeable.
        #myactbook.accountsList = {} #dict
                        #bbean_pwManKey.bean
                        #bbean_pwManData.bean
        # Instance the Fernet class with the key
        myactbook.sessionKey = Fernet.generate_key().decode('utf-8')
        #myactbook.fernet = Fernet(myactbook.sessionKey)
        #newEntry = accountEntry()
        #list
        #myactbook.accountsList.append(json.dumps(newEntry.__dict__))
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
#Getters
    def getAccountKey(myactbook):
        return myactbook.accountKey
    def getAccountEmail(myactbook):
        return myactbook.accountEmail
    def getSessionKey(myactbook):
        return myactbook.sessionKey
    def getSessionFile(myactbook):
        return myactbook.sessionFile
    def getAccountEntryList(myactbook):
        accountEntryList = []
        for entryText in myactbook.accountsList:
            newEntry = accountEntry()
            newEntry.loadEntry(entryText)
            #entryTextDict = json.loads(entryText)
            #newEntry.setAccountHolder = entryTextDict["accountHolder"]
            #newEntry.setUsername = entryTextDict["username"]
            #newEntry.setEmail = entryTextDict["email"]
            #newEntry.setPassword = entryTextDict["password"]
            accountEntryList.append(newEntry)
        return accountEntryList
#Setters
    def setAccountKey(myactbook, input):
        myactbook.accountKey = input
    def setAccountEmail(myactbook, input):
        myactbook.accountEmail = input
    def setSessionKey(myactbook, input):
        myactbook.sessionKey = input
    def setSessionFile(myactbook, input):
         myactbook.sessionFile = input
#Utility
    def toString(myactbook):    #Lets base our save format off of json for easy transfer between python and java.
        jsonstr1 = json.dumps(myactbook.__dict__)
        return jsonstr1
    def addEntry(myactbook, account, username, password):
        print("---Start: addEntry")
        #account = input("Please enter account: ")
        #username = input("Please enter username: ")
        #password = input("Please enter password: ")
        
        #encAccount = fernet.encrypt(account.encode())
        #encUsername = fernet.encrypt(username.encode())
        #encPassword = fernet.encrypt(password.encode())
        #print("original password: ", password)
        #print("encrypted encPassword: ", encPassword)

        newEntry = accountEntry()
        newEntry.setAccountHolder(account)
        newEntry.setUsername(username)
        if (myactbook.accountEmail):
            newEntry.setEmail(myactbook.accountEmail)
        newEntry.setPassword(password)
        #myactbook.accountsList[newEntry.getAccountHolder()] = newEntry
        myactbook.accountsList.append(json.dumps(newEntry.__dict__))
        return newEntry.toString()
    def removeEntry(myactbook, selection):
        myactbook.accountsList.pop(selection-1)
    def load(myactbook, accountBookText):
        #Convert JsonObjTxt to PyDict
        abtJson = json.loads(accountBookText)
        #print("JSON string = ", abtJson)
        #print("JSON accountEmail = ", len(abtJson["accountEmail"]))
        
        #Convert 
        if  len(abtJson["accountKey"])>= 0:
            savedKey = abtJson["accountKey"]
            #print("KEY string: ", savedKey)
            myactbook.setAccountKey(savedKey)
        if  len(abtJson["accountEmail"]) >= 0:
            savedEmail = abtJson["accountEmail"]
            #print("Email string: ", savedEmail)
            myactbook.setAccountEmail(savedEmail)
        if  len(abtJson["sessionKey"]) >= 0:
            savedSesKey = abtJson["sessionKey"]
            #print("Session Key string: ", savedSesKey)
            myactbook.setSessionKey(savedSesKey)
        if  len(abtJson["sessionFile"]) >= 0:
            savedfile = abtJson["sessionFile"]
            #print("savedfile string: ", savedfile)
            myactbook.setAccountKey(savedKey)
        if  len(abtJson["accountsList"]) >= 0:
            savedList = abtJson["accountsList"]
            #print("savedList string: ", savedList)
            for account in savedList:
                aetJson = json.loads(account) 
                #print("account json string: ", aetJson)
                tempActEntry = accountEntry()
                tempActEntry.loadEntry(aetJson)
                #print("myAccountEntry.toString(): ", tempActEntry.toString())
                myactbook.accountsList.append(json.dumps(tempActEntry.__dict__))
        
        
        
    def listEntries():
        print("---Start: listEntries")
    def editEntry(myactbook):
        print("---Start: editEntry")