import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import urlparse, parse_qs
import http.client

PORT = 8080

#ME FALTA COMMANDS DE ANTONIO Q LO HAA HECHO PATI TMBN PARA URL Y JASON

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        query = url_path.query

        try:
            route = self.requestline.split(" ")[1]
            filename = route[1:]
        except IndexError:
            route = "/"

        if route == "/" or route == "/favicon.ico":
            contents = Path("index.html").read_text()
            contents = j.Template(contents)

        elif route == "/species":
            try:
                ENDPOINT = "/info/species"
                PARAMS = "?content-type=application/json"

                s = commands.make_ensembl_request(ENDPOINT, PARAMS)
            except ValueError:
                contents = Path("error.html").read_text()
                contents = j.Template(contents)

        elif route == "karyotype":
            try:
                ENDPOINT = "info/assembly_info"
                PARAMS = "?content-type=application/json"
                s = commands.make_ensembl_request(ENDPOINT, PARAMS)
            except KeyError:
                contents = Path("error.html").read_text()
                contents = j.Template(contents)
        else:
            try:
                contents = Path("info/" + filename + ".html").read_text()
            except FileNotFoundError:
                contents = Path("error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()