#Purpose: Simple program to store passwords in an encrypted format
from cryptography.fernet import Fernet
from datetime import datetime



sessionKey = ""
sessionFile = ""#savKey2023-09-24_19.21.58.475349.bean.txt



def write(filename, value):
	print("Start Write")
	with open(filename+".txt", mode="at") as f:
		f.write(value+"\n")
	
def read(filename):
	print("-----Start Read")
	with open(filename, mode="rt") as f:
		lines = f.readlines()
		for line in lines:
			print(line.strip()) # strip() removes "\n"
	print("-----End Read")
	return lines;
	
def add():
	global sessionKey
	# datetime object containing current date and time
	now = datetime.now()
	#print("now =", now)
	
	account = input("Please enter account: ")
	username = input("Please enter username: ")
	password = input("Please enter password: ")
	
	
	filename = "savKey"+str(now)+".bean"
	filename = filename.replace(" ", "_")#replace spaces w/ "_"
	filename = filename.replace(":", ".")#replace ":"s in time w/ "."
	print(sessionKey)
	if len(sessionKey) < 10:
		newKyQ = input("You do not have a Key loaded.\nWould you like to create a (N)ew Key, or (L)oad an existing Key? ")
		match newKyQ:
			case "N":#List
				sessionKey = Fernet.generate_key()
			case "L":
				load()
	
	
	# Instance the Fernet class with the key
	fernet = Fernet(sessionKey)
	# then use the Fernet class instance
	# to encrypt the string string must
	# be encoded to byte string before encryption
	encAccount = fernet.encrypt(account.encode())
	encUsername = fernet.encrypt(username.encode())
	encPassword = fernet.encrypt(password.encode())
	print("original password: ", password)
	print("encrypted encPassword: ", encPassword)

	write(filename,"PWM:KEY:"+str(sessionKey))
	write(filename,"PWM:ACCT:"+str(account))
	write(filename,"PWM:USRNM:"+str(username))
	write(filename,"PWM:ENCPW:"+str(encPassword))

def load():
	fileSelect = input("Load File: ")
	lines = read(fileSelect)
	for line in lines:
		line = line.strip()
		if  line.find("KEY") >= 0:
			savedKey = line[line.find("KEY")+6:-1]
			print("KEY string: ", savedKey)
		if  line.find("ACCT") >= 0:
			savedAcct = line[line.find("ACCT")+5:]
			print("ACCT string: ", savedAcct)
		if  line.find("USRNM") >= 0:
			savedUsrnm = line[line.find("USRNM")+6:]
			print("savedKey string: ", savedUsrnm)
		if  line.find("ENCPW") >= 0:
			savedEncMessage = line[line.find("encMessage")+6:-1]
			print("savedEncMessage string: ", savedEncMessage)
		if  line.find("encMessage") >= 0:
			encMessage = line[line.find("encMessage")+13:-1]
			print("encMessage string: ", encMessage)
	global sessionKey
	global sessionFile
	sessionKey = savedKey;
	sessionFile = fileSelect;
	
def list():
	fileSelect = input("File to List: ")
	lines = read(fileSelect)
	for line in lines:
		line = line.strip()
		if  line.find("KEY") >= 0:
			savedKey = line[line.find("KEY")+6:-1]
			print("KEY string: ", savedKey)
		if  line.find("ACCT") >= 0:
			savedAcct= line[line.find("ACCT")+5:]
			print("ACCT string: ", savedAcct)
		if  line.find("USRNM") >= 0:
			savedUsrnm = line[line.find("USRNM")+6:]
			print("USRNM string: ", savedUsrnm)
		if  line.find("ENCPW") >= 0:
			savedEncpw = line[line.find("ENCPW")+6:-1]
			print("ENCPW string: ", savedEncpw)
		if  line.find("encMessage") >= 0:
			encMessage = line[line.find("encMessage")+13:-1]
			print("encMessage string: ", encMessage)
		#print(line.strip()) # strip() removes "\n"

def pull():
	fileSelect = input("File to List: ")
	lines = read(fileSelect)
	for line in lines:
		line = line.strip()
		if  line.find("KEY") >= 0:
			savedKey = line[line.find("KEY")+6:-1]
			print("KEY string: ", savedKey)
		if  line.find("ACCT") >= 0:
			savedAcct= line[line.find("ACCT")+5:]
			print("ACCT string: ", savedAcct)
		if  line.find("USRNM") >= 0:
			savedUsrnm = line[line.find("USRNM")+6:]
			print("USRNM string: ", savedUsrnm)
		if  line.find("ENCPW") >= 0:
			savedEncpw = line[line.find("ENCPW")+8:-1]
			if len(savedKey) < 3:
				print("no key found")
				print("ENCPW string: ", savedEncpw)
			else:
				print("ENCPW string: ", savedEncpw)
				print("savedKey string: ", savedKey)
				fernet = Fernet(savedKey)
				decMessage = fernet.decrypt(savedEncpw.encode()).decode()
				print("decrypted pw string: ", decMessage)
		if  line.find("encMessage") >= 0:
			encMessage = line[line.find("encMessage")+13:-1]
			print("encMessage string: ", encMessage)
		#print(line.strip()) # strip() removes "\n"
	#pullSelect = input("Select an entry to decode")
	# decrypt the encrypted string with the
	# Fernet instance of the key,
	# that was used for encrypting the string
	# encoded byte string is returned by decrypt method,
	# so decode it to string with decode methods
	#decMessage = fernet.decrypt(encMessage).decode()
	#print("decrypted string: ", decMessage)
	#print("savMessage string: ", savMessage)


###Start Main
print("Hello, welcome to the PW Manager")

#sessionKey = ""
#sessionFile = ""#savKey2023-09-24_19.21.58.475349.bean.txt
menuSelect = 1


while int(menuSelect) > 0:
	print("sessionKey string: ", sessionKey)
	print("sessionFile string: ", sessionFile)
	menuSelect = input("Menu: \n 1: List\n 2: Pull\n 3: Add\n 4: Load\n 0: EXIT\n")
	match menuSelect:
		case "1":#List
			print("List Lines: \n")
			list()
		case "2":#Pull
			print("Choose an acct to pull the pw for")
			pull()
		case "3":#Add
			print("Add new Entry")
			add()
		case "4":#Load
			load()
		case "0":
			print("Exit")
			break
		case _:
			print("The selection doesn't matter, what matters is solving problems.")
			break
#



