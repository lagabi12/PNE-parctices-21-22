from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"

seq = "../P0/P0/sequences/FRAT1"
s = Seq()
seq = s.read_fasta(seq)
bases = 10
fragments = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"Sending FRAT1 in segments of 10 to server...")
for f in fragments:
    frag = seq[f*bases:bases*(f+1)]
    if (f+1) % 2 == 0:
        PORT = 8080
        c = Client(IP, PORT)
        c.debug_talk("Fragment "+ str(f+1) + ": " + frag)
    else:
        PORT = 8083
        c = Client(IP, PORT)
        c.debug_talk("Fragment "+ str(f+1) + ": " + frag)