from cryptography.fernet import Fernet
from datetime import datetime



def decodeValue():
	value = "PASSWORD"
	print("decrypted string: ")
	
	
	
def write(filename, value):
	print("Start Write")
	with open(filename+".txt", mode="at") as f:
		f.write(value+"\n")
	
def read(filename):
	print("Start Read")
	with open(filename, mode="rt") as f:
		lines = f.readlines()
		for line in lines:
			print(line.strip()) # strip() removes "\n"
	return lines






# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)



# we will be encrypting the below string.
message = "hello geeks"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()
print("original key: ", key)
# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)

filename = "savKey"+str(now)+".bean"
filename = filename.replace(" ", "_")
filename = filename.replace(":", ".")


write(filename,"PWM:KEY:"+str(key))
write(filename,"PWM:encMessage:"+str(encMessage))
lines = read("savKey2023-09-24_03.27.33.580518.bean.txt")

for line in lines:
	line = line.strip()
	if  line.find("KEY") >= 0:
		savedKey = line[line.find("KEY")+6:-1]
		print("savedKey string: ", savedKey)
	if  line.find("encMessage") >= 0:
		savedEncMessage = line[line.find("encMessage")+13:-1]
		print("savedEncMessage string: ", savedEncMessage)
	#print(line.strip()) # strip() removes "\n"
			
fernetSav = Fernet(savedKey)
savMessage = fernetSav.decrypt(savedEncMessage).decode()



print("savMessage string: ", savMessage)