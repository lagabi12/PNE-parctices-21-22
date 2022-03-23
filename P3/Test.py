from Client import Client
IP = "127.0.0.1"
PORT = 5678
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU"]
c = Client(IP, PORT)
print(c)

print("Testing PING...")
c.debug_talk("PING")
print("Testing GET...")
for i in range(5):
    c.debug_talk("GET " + str(i))
seq = c.debug_talk("GET 0").replace("GET0:", "")
print("Testing INFO...")
c.debug_talk(f"INFO {seq}")
print("Testing COMP...")
c.debug_talk(f"COMP {seq}")
print("Testing REV...")
c.debug_talk(f"REV {seq}")
print("\nTesting GENE...")
for g in GENES:
    print(g)
    c.debug_talk(f"GENE {g}")

msg = input("Message for the server: ")
print("FUNCTION ADD: ")
c.debug_talk(msg)



