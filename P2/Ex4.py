from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)

FOLDER = "../P0/P0/sequences/"
sequences = ["FRAT1", "ADA", "FXN"]

for r in sequences:
    filename = FOLDER + r
    s = Seq()
    seq = s.read_fasta(filename)
    c.debug_talk(f"Sending {r} gene to server...")
    c.debug_talk(str(seq))
    response = c.talk(f"Sending {r} gene to server...")