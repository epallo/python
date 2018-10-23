import os
import socket
print("")
print("The home directory is "+os.path.expanduser('~'))
print("The system hostname is "+socket.gethostname())
print("The system IP address is "+socket.gethostbyname(socket.gethostname()))
print("The current working directory is "+os.getcwd())