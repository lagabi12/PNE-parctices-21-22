import socket
from colorama import init, Fore
from Seq1 import Seq

PORT = 5678
IP = "127.0.0.1"

seq1 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
seq2 = "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA"
seq3 = "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT"
seq4 = "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA"
seq0 = "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"

sequences = (seq0, seq1, seq2, seq3, seq4)
BASES = ["A", "C", "T", "G"]
FOLDER = "../P0/P0/sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU"]
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    serversocket.bind((IP, PORT))
    serversocket.listen()
    print("Server configured!")
    print("Waiting for clients...")

    while True:
        init(autoreset=True)
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        print("A client has connected to the server!")

        # Read the message from the client
        msg = clientsocket.recv(2048).decode("utf-8")

        # Send the message
        slices = msg.split(" ")
        command = slices[0]
        if len(slices) >= 2:
            arg = slices[1]
        else:
            arg = "none"

        if command == "PING":
            print("PING command!".format(Fore.LIGHTYELLOW_EX))
            response = f"OK!\n"

        elif command == "GET":
            print("GET".format(Fore.LIGHTYELLOW_EX))
            if 0 <= int(arg) <= 4:
                response = sequences[int(arg)]
            else:
                response = "Argument must be an int between 0 and 4"

        elif command == "INFO":
            print("INFO".format(Fore.LIGHTYELLOW_EX))
            bases = ""
            valid = Seq.valid_sequence(arg)
            length = str(Seq.len(arg, valid))
            for base in BASES:
                info = Seq.count_base(arg, base)
                bases += base + ": " + str(info[0]) + "(" + str(info[1]) + "%) \n"
            response = "Total length: " + length + "\n" + bases

        elif command == "COMP":
            print("COMP".format(Fore.LIGHTYELLOW_EX))
            valid = Seq.valid_sequence(arg)
            response = Seq.complement(arg, valid)

        elif command == "REV":
            valid = Seq.valid_sequence(arg)
            if valid:
                print("REV".format(Fore.LIGHTYELLOW_EX))
                response = Seq.reverse(arg, valid)
            elif arg in GENES:
                print("GENE".format(Fore.LIGHTYELLOW_EX))
                s = Seq()
                response = Seq.read_fasta2(FOLDER + arg)
            else:
                response = "File not found"

        else:
            response = "Command not available in this server\n"

        print(response)
        try:
            send_bytes = str.encode(Fore.LIGHTGREEN_EX + response)
            clientsocket.send(send_bytes)
            clientsocket.close()
            serversocket.close()

            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serversocket.bind((IP, PORT))
            serversocket.listen()
            print("Waiting for clients...")

        except TypeError:
            pass

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()