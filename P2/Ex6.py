from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"



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
print("Sending FRAT1 gene to the server, in fragments of 10 bases:")
i = 1
times = 0
for f in sequences:
    if i % 2 == 0:
        PORT = 1111
        c = Client(IP, PORT)
        print(f"Sending Fragment: " + str(i), f)
        response = c.talk("Fragment " + str(i))
        i = i + 1
    else:
        PORT = 2222
        # -- Print the IP and PORTs
        c = Client(IP, PORT)
        print(f"Sending Fragment: " + str(i),  f)
        response = c.talk("Fragment " + str(i))
        i = i + 1