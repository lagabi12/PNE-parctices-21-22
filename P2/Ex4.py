from Client0 import Client
from Seq1 import Seq
import colorama

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)
print(c)

seq0 = "FRAT1"
seq1 = "ADA"
seq2 = "FXN"
FOLDER = "../P0/P0/sequences/"

sequences = [seq0, seq1, seq2]
for r in sequences:
    s = Seq()
    s.read_fasta(FOLDER + r)
    print(f"Sending {colorama.Fore.BLUE + r } to the server..." + colorama.Fore.RESET)
    response = c.talk(f"Sending {r} gene to server" + colorama.Fore.RESET)
    print(f"Response: {colorama.Fore.YELLOW + response + colorama.Fore.RESET}")
    print(f"Sending {colorama.Fore.BLUE + str(s) } to the server..." + colorama.Fore.RESET)
    response = c.talk(s.strbases)
    print(f"Response: {colorama.Fore.YELLOW + response + colorama.Fore.RESET}")