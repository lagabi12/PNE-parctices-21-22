from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)

file = "../P0/P0/sequences/FRAT1"
s = Seq()
seq = s.read_fasta(file)

bases = 10
fragments = (0, 1, 2, 3, 4)

c.debug_talk(f"Sending FRAT1 in segments of 10 to server...")
for f in fragments:
    frag = seq[f*bases:bases*(f+1)]
    c.debug_talk("Fragment"+ str(f+1) + ": " + frag)


