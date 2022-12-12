from socket import *
import sys # In order to terminate the program
import threading
import time

#Assigns a port number
#Binds the socket to server address and server port
#Tells the socket to listen to at most 1 connection at a time

serverSocket = socket(AF_INET, SOCK_STREAM)
PORT = 8037
SERVER = gethostbyname(gethostname())
serverSocket.bind((SERVER,PORT))


#handles individual connection between client and server; runs for each client                  
def handle_client(connectionSocket, addr):
    print(f"[New Connection] {addr} connected")
    connected = True 
  
#Receives the request message from the client
    message = connectionSocket.recv(1024) 
        # print(f"[{addr}] {message}")
    print(message)

    try:

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes 
        # a character '\', we read the path from the second character
        f = open(filename[1:])
        

        outputdata = f.read()
        #print(outputdata)
        time.sleep(7)
        
        None # TODO: Store the entire contents of the requested file in a temporary buffer


        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
            # TODO: Send one HTTP header line into socket

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        print(f"Connection {addr} closed")
        connected = False

    except IOError as err:
        print(err)

        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
            # TODO: Send response message for file not found
            #       Close client socket
        connectionSocket.close()


#Sets up a new connection from the client
#handles new connections and distributes them 
def start():
    serverSocket.listen(1)
    print(f"[LISTENING] server is listening on {SERVER}")
    while True: 
        connectionSocket, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(connectionSocket,addr))
        thread.start()

    #there's always an active thread, the rest are connected clients
        print(f"[Active Connections] {threading.active_count() -1}")
        

print('Ready to serve...') 
start()


# serverSocket.close()
# sys.exit()  #Terminate the program after sending the corresponding data
