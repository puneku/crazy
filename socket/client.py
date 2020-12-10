import socket

# create socket at client side
cs = socket.socket()

# connect client to server
cs.connect(("localhost", 12345))

# print received data
print(cs.recv(1024).decode())

