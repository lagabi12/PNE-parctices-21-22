from Client0 import Client
from Seq1 import Seq
import colorama

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to



seq = "../P0/P0/sequences/FRAT1"
s = Seq()
s.read_fasta(seq)
frag1 = str(s)[:10]
frag2 = str(s)[11:20]
frag3 = str(s)[21:30]
frag4 = str(s)[31:40]
frag5 = str(s)[41:50]
frag6 = str(s)[51:60]
frag7 = str(s)[61:70]
frag8 = str(s)[71:80]
frag9 = str(s)[81:90]
frag10 = str(s)[91:100]

sequences = [frag1, frag2, frag3, frag4, frag5, frag6, frag7, frag8, frag9, frag10]


i = 1
times = 0
for o in sequences:
    if i == 1 or i == 3 or i==5 or i==7 or i== 9:
        IP = "127.0.0.1"
        PORT = 8080
        # -- Print the IP and PORTs
        c = Client(IP, PORT)
        if times < 1:
            print(f"Gene FRAT1 {colorama.Fore.BLUE + str(s)} to the server in fragments of 10 bases..." + colorama.Fore.RESET)
            response = c.talk(f"Sending {seq} gene to server" + colorama.Fore.RESET)
            times += 1
        print(f"Sending Fragment" + str(i) + f":{colorama.Fore.BLUE + o} to the server..." + colorama.Fore.RESET)
        response = c.talk("Sending Fragment" + str(i) + f": {i} gene to server" + colorama.Fore.RESET)
        i = i + 1
    elif i != 1 or i != 3 or i != 5 or i != 7 or i != 9:
        IP = "127.0.0.1"
        PORT = 8081
        # -- Print the IP and PORTs
        c = Client(IP, PORT)
        print(f"Sending Fragment" + str(i) + f":{colorama.Fore.BLUE + o} to the server..." + colorama.Fore.RESET)
        response = c.talk("Sending Fragment" + str(i) + f": {i} gene to server" + colorama.Fore.RESET)
        i = i+1