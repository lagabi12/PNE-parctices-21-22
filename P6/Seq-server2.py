import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        seq_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA","AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA","CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT","CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA","AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
        termcolor.cprint(self.requestline, 'green')

        try:
            route = self.requestline.split(" ")[1]
            filename = route[1:]
            print("FILENAME", filename)

        except IndexError:
            route = "/"

        try:
            filename = filename.split("?")[1]
            filename = filename.split("&")

            command_dict = {}
            for i in filename:
                i = i.split("=")
                command_dict[i[0]] = i[1]
            print(command_dict)

        except IndexError:
            pass

        termcolor.cprint(filename, "blue")

        if route == "/" or route == "/favicon.ico":
            contents = Path("index.html").read_text()

        elif "/ping" in route:
            contents = Path("PING.html").read_text()

        elif "/get?" in route:
            n = int(command_dict["number"])
            seq = seq_list[int(command_dict["number"])]
            contents = Path("GET.html").read_text().format(n=n, seq=seq)

        elif "/gene?" in route:
            gene = command_dict["gene"]
            seq = Seq()
            file = "./sequences/" + gene
            seq.read_fasta(file)
            gene_seq = seq.format_txt()

            contents = Path("GET.html").read_text().format(n=gene, seq=seq)

        elif "/operation?" in route:
            command = command_dict["operation"]
            arg = command_dict["seq"]
            if not Seq(arg).valid_sequence():
                contents = "Incorrect sequence, please enter a correct sequence"

            elif command == "INFO":
                new_seq = Seq(arg)
                n_bases = new_seq.bases()
                percentages = new_seq.base_percentage()
                seq_len = new_seq.len()

                contents = "Sequence: " + arg

                contents = contents + "\nTotal lenght: " + str(seq_len) + "\n"

                for k in percentages:
                    contents = contents + str(k) + ": " + str(n_bases[k]) + " (" + str(percentages[k]) + "%)\n"

            elif command == "COMP":
                contents = Seq(arg).seq_complement() + "\n"

            elif command == "REV":
                contents = Seq(arg).seq_reverse() + "\n"

            contents = contents.replace("\n", "<p><p>")
            contents = Path("OPERATIONS.html").read_text().format(op=command, result=contents, seq=arg)

        else:
            contents = Path("error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()