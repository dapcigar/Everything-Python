import socket as clientsock

# create a socket object
serversocket = clientsock.socket(clientsock.AF_INET, clientsock.SOCK_STREAM)
# get local machine address
host = clientsock.gethostname()
port = 9999
# connect to Server hostname and port
serversocket.connect((host, port))
# Receieve no more than 1024 bytes
msg = serversocket.recv(1024)
print(msg)
serversocket.close()
