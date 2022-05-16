import http.client
import json
from Seq1 import Seq
import termcolor

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'

GENES = {"SCRAP": "ENSG00000080603",
         "FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

BASES = ["A", "G", "C", "T"]

gene = input("Gene name:")
print(f"\nConnecting to server: {SERVER}\n")

for k, v in GENES.items():
    if k == gene:
        id = v

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + id + PARAMS)
except ConnectionRefusedError:
    termcolor.cprint("ERROR! Cannot connect to the Server", "red")
    exit()
except TypeError:
    termcolor.cprint("Gene not found", "red")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)
bases = data1["seq"]

s = Seq(bases)
s.valid_sequence()
length = s.length()

termcolor.cprint("Gene:", "green", end="")
print(gene)
termcolor.cprint("Description:", "green", end="")
print(data1["desc"])
termcolor.cprint("Bases:", "green", end="")
print(bases)
termcolor.cprint("Total length:", "green", end="")
print(length)

for b in BASES:
    percentage = str(round(s.count_base(b)/length * 100, 2))
    termcolor.cprint(b, "blue", end=": ")
    print(str(s.count_base(b)) + "(" + percentage + "%)")

termcolor.cprint("Most frequent:", "green", end="")
print(s.frequent_base())



