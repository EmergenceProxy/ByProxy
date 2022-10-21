#Purpose: Port scanner project
#Take target. Input or file.
#Scan ports. Quick scan, common ports. medium, 10k. Long scan, all ports.
#Output. To screen, save to doc.
import pyfiglet
import sys
import socket
import os
from datetime import datetime



ascii_banner = pyfiglet.figlet_format("Bean Port Scanner")
print(ascii_banner)
#host = input(str("Input Target IP: "));
host = "70.108.16.201"
host = socket.gethostname()

#Banner
print("_"*50)
print("Scanning target: " +host)
print("Scan Start: " + str(datetime.now()) )
print("_"*50)
openports="Open Ports: \n"

window = ascii_banner
window += str("_"*50)+ "\n"
window += str("Scanning target: " +host)+ "\n"
window += str("Scan Start: " + str(datetime.now()) )+ "\n"
window += str("_"*50)+ "\n"


try:
    for port in range(1,65535):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3)
        
        result = s.connect_ex((host,port))
        print("Scanning port: " +str(port) )
        
        if result == 0:
            openports+="[*] Port {} is open\n".format(port)
            
        os.system('cls')
        if(len(openports) > 14):
            print(window+openports)
        else:
            print(window)
        s.close
       
    print("Scan complete: " + str(datetime.now()) )       
        
except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit
    
except socket.error:
    print("\ Host not resoponding :(")
    sys.exit