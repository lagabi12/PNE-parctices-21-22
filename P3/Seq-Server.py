import socket
from Seq1 import Seq
import termcolor

PORT = 5678
IP = "127.0.0.1"

seq1 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
seq2 = "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA"
seq3 = "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT"
seq4 = "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA"
seq0 = "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
sequences = (seq0, seq1, seq2, seq3, seq4)
BASES = ["A", "C", "T", "G"]
FOLDER = "./sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU"]

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    serversocket.bind((IP, PORT))
    serversocket.listen()
    print("Server configured!")
    print("Waiting for clients...")

    while True:
        # accept connections
        (clientsocket, address) = serversocket.accept()
        print("A client has connected to the server!")
        # Read the message
        msg = clientsocket.recv(2048).decode("utf-8")

        # Send the message
        slices = msg.split(" ")
        command = slices[0]
        if len(slices) >= 2:
            arg = slices[1]
        else:
            arg = "none"

        if command == "PING":
            termcolor.cprint("PING", "yellow")
            response = f"OK!\n"

        elif command == "GET":
            termcolor.cprint("GET", "yellow")
            if 0 <= int(arg) <= 4:
                response = sequences[int(arg)]
            else:
                response = "Argument must be an int between 0 and 4"

        elif command == "INFO":
            termcolor.cprint("INFO", "yellow")
            bases = ""
            valid = Seq.valid_sequence(arg)
            if valid:
                length = str(Seq.len(arg, valid))
                for base in BASES:
                    info = Seq.count_base(arg, base)
                    bases += base + ": " + str(info[0]) + "(" + str(info[1]) + "%) \n"
                response = "Total length: " + length + "\n" + bases
            else:
                response = "Not a valid sequence"

        elif command == "COMP":
            termcolor.cprint("COMP", "yellow")
            valid = Seq.valid_sequence(arg)
            if valid:
                response = Seq.complement(arg, valid)
            else:
                response = "Not a valid sequence"

        elif command == "REV":
            valid = Seq.valid_sequence(arg)
            if valid:
                termcolor.cprint("REV", "yellow")
                response = Seq.reverse(arg, valid)

        elif command == "GENE":
            if arg in GENES:
                termcolor.cprint("GENE", "yellow")
                s = Seq()
                filename = FOLDER + arg
                s.read_fasta(filename)
                response = str(s)
            else:
                response = "File not found"

        else:
            response = "Command not available in this server\n"

        print(response)
        try:
            send_bytes = str.encode(response)
            clientsocket.send(send_bytes)
            clientsocket.close()
            print("Waiting for clients...")
        except TypeError:
            pass

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))
except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()