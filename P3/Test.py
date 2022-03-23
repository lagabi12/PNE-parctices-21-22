from Client import Client
IP = "127.0.0.1"
PORT = 5678

c = Client(IP, PORT)
print(c)
msg = input("Message for server: ")
c.debug_talk(msg)
response = c.talk(msg)

COMMANDS = ("PING", "GET", "INFO", "COMP", "REV")
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU"]
numbers = ["0", "1", "2", "3"]
seq = c.debug_talk("GET 0")

for c in COMMANDS:
    print(" * TESTING", c, "...")
    if c == "PING":
        msg = "PING"


    elif c == "GET":
        for n in numbers:
            msg = "GET " + n
    elif c == "INFO":
        msg = "INFO " + seq
    elif c == "COMP":
        msg = "COMP " + seq
    elif c == "REV":
        msg = "REV " + seq
    elif c == "GENE":
        for g in GENES:
            msg = "GENE" + g

