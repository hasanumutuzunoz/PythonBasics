import socket

host = "localhost"
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print("Server listening on port:", port)

c, addr = s.accept()

fileName = c.recv(1024)             # Receive file name from client
try:                                # If file exists
    f = open(fileName, 'rb')        # Open the file, rb --> Read Binary
    content = f.read()              # Read the file
    c.send(content)                 # Send the content to client
    f.close()                       # Close the file
except FileNotFoundError:           # If there is no file give error
    c.send(b"File does not exist")  # Send client a message

c.close()