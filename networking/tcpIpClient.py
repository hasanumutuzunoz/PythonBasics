import socket

s = socket.socket()

s.connect(("localhost", 4000))

# Receive 1024 bytes at time
msg = s.recv(1024)

# While we have message TRUE
while msg:
    print("Received: ", msg.decode())
    msg = s.recv(1024) #update msg with new message

s.close() # Close the connection