from Client import Client

IP = "127.0.0.1"
PORT = 8020

c = Client(IP, PORT)
print(c.seq_ping())