#!/bin/python

import sys
import socket
from datetime import datetime

#Define out target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translating Hostname to IPv4
else:
	print("Invalid amount of arguements")

#Add a pretty banner
print("-"*50)
print("Scanner target "+ target)
print("Timer started  " + str(datetime.now()))
print("-"*50)

try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		print("Checking port {} ".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt: 
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Host name could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()
