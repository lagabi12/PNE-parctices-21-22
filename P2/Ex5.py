from Client0 import Client
from Seq1 import Seq
import colorama

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 1111
# -- Print the IP and PORTs
c = Client(IP, PORT)
print(c)


seq = "../P0/P0/sequences/FRAT1"
s = Seq()
s.read_fasta(seq)
frag1 = str(s)[:10]
frag2 = str(s)[11:20]
frag3 = str(s)[21:30]
frag4 = str(s)[31:40]
frag5 = str(s)[41:50]

sequences = [frag1, frag2, frag3, frag4, frag5]

print(f"Gene FRAT1 {colorama.Fore.BLUE + str(s) } to the server in fragments of 10 bases..." + colorama.Fore.RESET)

i = 1
for r in sequences:
    print(f"Sending Fragment" + str(i) + f":{colorama.Fore.BLUE + r } to the server..." + colorama.Fore.RESET)
    response = c.talk("Sending Fragment" + str(i) + f": {r} gene to server" + colorama.Fore.RESET)
    i = i + 1