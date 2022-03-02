from Client0 import Client
PRACTICE = 2
EXERCISE = 1
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45"
PORT = 8080
# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.seq_ping()

# -- Print the IP and PORTs
print("IP:", IP, ",", PORT)