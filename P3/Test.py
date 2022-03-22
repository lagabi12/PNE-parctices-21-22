from Client import Client
IP = "127.0.0.1"
PORT = 7470

c = Client(IP, PORT)
print(c)
msg = input("Message for server: ")
c.debug_talk(msg)
response = c.talk(msg)