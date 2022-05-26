import json
import http.client
from clientclass import Client
import termcolor as t

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)

def request_server(ENDPOINT, PARAMS=""):
    try:
        connection = http.client.HTTPConnection(IP, PORT)
        try:
            connection.request("GET", ENDPOINT + PARAMS)
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()
        r1 = connection.getresponse()
        print(f"Response received!: {r1.status} {r1.reason}\n")
        data1 = r1.read().decode("utf-8")
        data2 = json.loads(data1)
        return data2
    except Exception:
        print({"error": "ERROR"})

t.cprint("LIST OF SPECIES:", "green")
limit = input("Enter a limit: ")
list_species = request_server("/species?","limit="+limit+"&json=on")
t.cprint(list_species, "blue")

t.cprint("KARYOTYPE:", "green")
species = input("Enter a species: ")
karyotype = request_server("/karyotype?", "species="+species+"&json=on")
t.cprint(karyotype, "blue")

t.cprint("LENGTH:", "green")
species = input("Enter a species: ")
chromosome = input("Enter a chromosome: ")
chrom_length = request_server("/chromosomeLength?", "specie="+species+"&chromosome="+chromosome+"&json=on")
t.cprint(chrom_length, "blue")

t.cprint("SEQUENCE:", "green")
gene = input("Enter human gene:")
seq = request_server("/geneSeq?", "gene="+gene+"&json=on")
t.cprint(seq, "blue")

t.cprint("INFO:", "green")
gene = input("Enter human gene:")
info = request_server("/geneInfo?", "gene="+gene+"&json=on")
t.cprint(info, "blue")

t.cprint("THE CALCULATIONS ARE:", "green")
gene = input("Enter human gene:")
calculations = request_server("/geneCalc?", "gene="+gene+"&json=on")
t.cprint(calculations, "blue")

t.cprint("LIST OF GENES:", "green")
chromosome = input("Enter a chromosome:")
start = input("Start point:")
end = input("End point:")
list_genes = request_server("/geneList?", "chromo="+chromosome+"&start="+start+"end="+end+"&json=on")
t.cprint(list_genes, "blue")

