import socket as sockapp

serversocket = sockapp.socket(sockapp.AF_INET, sockapp.SOCK_STREAM)
host = sockapp.gethostname()
port = 9999
serversocket.bind((host, port))

# Queue up to 5 times
serversocket.listen(5)
while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting ' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
