import socket

host = "localhost"
port = 4000

#socket.AF_INET ---> internet protocol version 4
#socket.SOCK_STREAM ---> tcpIP connection
#These parameters are by default so we don't need to write them
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to a host and port
s.bind((host,port))

# Start the server to listen to a host on the port
# Parameter 1 is the number of connections (clients) this server is going to accept
s.listen(1)
print("Server listening on port:", port)

# When the client connects to the server, accept
# c, addr --- > Return connection and client's address
c, addr = s.accept()

print("connection from:", str(addr))

# Encode the message, Convert to binary with b or encode()
c.send(b"Hello, how are you?")
c.send("bye".encode())
c.close()