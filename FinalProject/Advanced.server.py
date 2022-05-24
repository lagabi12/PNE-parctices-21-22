import http.server
import socketserver
import termcolor
from pathlib import Path
import json
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
from Seq1 import Seq

SERVER = "rest.ensembl.org"
PORT = 8080
GENES = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296","RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}

def request_ensemble(ENDPOINT, PARAMS=""):
    connection = http.client.HTTPConnection(SERVER)
    try:
        parameters = "?content-type=application/json"
        connection.request("GET", ENDPOINT+parameters+PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = connection.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data2 = json.loads(data1)
    return data2

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler.
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        #urlparse te devuelve trozos del url en tuplas
        path = url_path.path
        #path es endpoint
        arguments = parse_qs(url_path.query)
        #query es string te da desde la interrogacion hasta el final
        #parse devuelve diccionario (argumento)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)

        if self.path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/species":
            species = []
            try:
                limit = int(arguments["limit"][0])
                species_dict = request_ensemble("/info/species", "")
                length = len(species_dict["species"])
                if 0 < limit <= length:
                    for n in range(0, limit):
                        species.append(species_dict["species"][n]["name"])
                    contents = read_html_file("listSpecies" + ".html")\
                     .render(context = {"limit": limit, "length": str(length), "list": species})
                else:
                    contents = read_html_file("error.html") \
                        .render(context={"error": "Please, enter a valid value for the limit, between 1 and " + str(length)})
            except ValueError:
                contents = read_html_file("error.html")\
                    .render(context={"error": "Please, enter a valid value for the limit"})
            except KeyError:
                contents = read_html_file("error.html")\
                    .render(context={"error": "Please, enter a value"})

        elif path == "/karyotype":
            try:
                species = arguments["species"][0]
                chromosomes_dict = request_ensemble("/info/assembly/" + species, "")
                chromosomes = chromosomes_dict["karyotype"]
                contents = read_html_file("karyotype" + ".html") \
                    .render(context={"species":chromosomes })
            except KeyError:
                contents = read_html_file("error.html")\
                    .render(context={"error": "Please, enter a valid specie"})

        elif path == "/chromosomeLength":
            try:
                specie = arguments["specie"][0]
                chromosome = arguments["chromosome"][0]
                chromosomes_dict = request_ensemble("/info/assembly/" + specie, "")
                dict_list = chromosomes_dict["top_level_region"]
                if 0 < int(chromosome) <= len(dict_list):
                    for c in dict_list:
                        if c["name"] == chromosome:
                            length = c["length"]
                    contents = read_html_file("chromosomeLength.html").render(context={"length": length})
                else:
                    contents = read_html_file("error.html") \
                        .render(context={"error": "Please, enter a valid chromosome: number between 0 and"+str(len(dict_list))})
            except KeyError:
                contents = read_html_file("error.html").render(context={"error": "Specie not found"})
            except ValueError:
                contents = read_html_file("error.html")\
                    .render(context={"error": "Please, enter a valid chromosome"})

        elif path == "/geneSeq":
            try:
                gene = arguments["gene"][0]
                if gene in GENES:
                    id = GENES[gene]
                    info_dict = request_ensemble("/sequence/id/"+ id, "")
                    seq = info_dict["seq"]
                    contents = read_html_file("geneSeq" + ".html") \
                        .render(context={"seq": seq, "gene": gene})
                else:
                    contents = read_html_file("error.html")\
                        .render(context={"error": "Gene not found"})
            except KeyError:
                contents = read_html_file("error.html").render(context={"error": "Please, enter a gene"})

        elif path == "/geneInfo":
            try:
                gene = arguments["gene"][0]
                if gene in GENES:
                    id = GENES[gene]
                    info_dict = request_ensemble("/sequence/id/" + id, "")
                    info = info_dict["desc"].split(":")
                    start = info[3]
                    end = info[4]
                    length = int(end) - int(start)
                    contents = read_html_file("geneInfo" + ".html") \
                        .render(context={"gene": gene, "id": id, "start": start, "end": end, "length": length})
                else:
                    contents = read_html_file("error.html") \
                        .render(context={"error": "Gene not found"})
            except KeyError:
                contents = read_html_file("error.html").render(context={"error": "Please, enter a gene"})

        elif path == "/geneCalc":
            try:
                gene = arguments["gene"][0]
                if gene in GENES:
                    id = GENES[gene]
                    info_dict = request_ensemble("/sequence/id/" + id, "")
                    seq = info_dict["seq"]

                    s = Seq(seq)
                    length = s.len()
                    bases = s.count_bases()
                    base = []
                    for d in bases:
                        base.append(str(bases[d][1]))

                    contents = read_html_file("geneCalc" + ".html") \
                        .render(context={"gene": gene, "length": length, "percentageA": base[0], "percentageC": base[1], "percentageG": base[2], "percentageT": base[3]})
                else:
                    contents = read_html_file("error.html") \
                        .render(context={"error": "Gene not found"})
            except KeyError:
                contents = read_html_file("error.html").render(context={"error": "Please, enter a gene"})

        elif path == "/geneList":
            try:
                chromo = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments["end"][0]
                region = chromo + ":" + start + "-" + end
                info_dict = request_ensemble("/phenotype/region/homo_sapiens/" + region, "")
                gene_list = []
                for gene_dict in info_dict:
                    for d in gene_dict["phenotype_associations"]:
                        if "attributes" in d:
                            if "associated_gene" in d["attributes"]:
                                gene_list.append(d["attributes"]["associated_gene"])
                if gene_list == []:
                    contents = read_html_file("geneList" + ".html").render(context={"genes": "No genes found"})
                else:
                    contents = read_html_file("geneList" + ".html").render(context={"genes": gene_list})
            except Exception:
                contents = read_html_file("error.html").render(context={"error": "Gene not found"})

        else:
            contents = "Information not available"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())
        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()