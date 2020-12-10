import socket

# create a server-side socket
ss = socket.socket()

# bind address(IP and PORT ) to server
ss.bind(("localhost", 12345))

# maximum 5 connection can connect
ss.listen(5)

print("Waiting to connect ...")

while True:
    # accept return client socket and address of client socket
    c, addr = ss.accept()
    print("connected with ",addr)
    c.send(bytes("Welcome to Puneku Server", "utf-8"))

    c.close()

