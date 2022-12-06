# Description:
# Port scanner to track network activity on the host
import pyfiglet
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
     
    # Map hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
 
# Displaying info about found ports
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))

try:
    # Scaning ports between 1 to 65,535
    for port in range(1, 65535):
        socket_var = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = socket_var.connect_ex((target, port))
        
        if result == 0:
            print("Port {} is open".format(port))
        socket_var.close()

except KeyboardInterrupt:
    print("Exiting the program")
    sys.exit()
except: socket.gaierror:
    print("Bad hostname. Could not be resolved")
    sys.exit()
except socket.error:
    print("Server not responding")
    sys.exit()


