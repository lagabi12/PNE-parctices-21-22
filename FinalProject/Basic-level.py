import http.server
import socketserver
import termcolor
from pathlib import Path
import json
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq
import http.client

SERVER = "rest.ensembl.org"
PORT = 8080
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


def convert_message(base_count): #CONVERTIMOS A STRING PARA MANDAR AL HTML
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" +"\n"
    return message


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
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
            limit = int(arguments["limit"][0])
            species_dict = request_ensemble("/info/species", "")
            length = len(species_dict["species"])
            if 0 < limit <= length and type(limit) == int:
                for n in range(0, limit):
                    species.append(species_dict["species"][n]["name"])
                contents = read_html_file("listSpecies" + ".html")\
                 .render(context = {"limit": limit, "length": str(length), "list": species
              })
            else:
                contents = read_html_file("error.html") \
                    .render(context={"error": "Please, enter a valid value for the limit, between 0 and " + str(length)})

        elif path == "/karyotype":
            species = arguments["species"][0]
            try:
                chromosomes_dict = request_ensemble("/info/assembly/" + species, "")
                chromosomes = chromosomes_dict["karyotype"]
                contents = read_html_file("karyotype" + ".html") \
                    .render(context={"species":chromosomes })
            except KeyError:
                contents = read_html_file("error.html") \
                    .render(context={"error": "Please, enter a valid specie"})

        elif path == "/chromosomeLength":
            specie = arguments["specie"][0]
            chromosome = arguments["chromosome"][0]
            try:
                chromosomes_dict = request_ensemble("/info/assembly/" + specie, "")
                dict_list = chromosomes_dict["top_level_region"]
                for c in dict_list:
                    if c == chromosome:
                        length = c["length"]
                contents = read_html_file("chromosomeLength.html") \
                    .render(context={"chromosome": length})
            except ValueError:
                contents = read_html_file("error.html") \
                    .render(context={"error": "Please, enter a valid specie"})

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

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()