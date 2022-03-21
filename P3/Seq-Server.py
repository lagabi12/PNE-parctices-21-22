import socket
from colorama import init, Fore
from Seq1 import Seq

PORT = 8020
IP = "127.0.0.1"

seq1 = "ATCGCCTA"
seq2 = "TCGCCTAA"
seq3 = "CGCCTAAT"
seq4 = "GCCTAATC"
seq0 = "CCTAATCG"
sequences = (seq0, seq1, seq2, seq3, seq4)
BASES = ["A", "C", "T", "G"]
FOLDER = "../P0/P0/sequences/U5"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    serversocket.bind((IP, PORT))
    print("Server configured!")
    print("Waiting for clients...")

    while True:
        init(autoreset=True)
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        print("A client has connected to the server!")

        # Read the message from the client
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(Fore.LIGHTYELLOW_EX + msg))

        # Send the message
        slice = msg.split(" ")
        command = slice[0]
        arg = slice[1]

        if command == "PING":
            print("PING command!".format(Fore.LIGHTGREEN_EX))
            response = f"OK!\n"

        elif command == "GET":
            print("GET command!".format(Fore.LIGHTGREEN_EX))
            if type(arg) == int and 0 <= int(arg) <= 4:
                arg = int(arg)
                response = sequences[arg]
            else:
                response = "Argument must be an int between 0 and 4"

        elif command == "INFO":
            length = Seq.len(arg)
            for base in BASES:
                bases = base + ": " + Seq.count_base(arg, base)
            response = length + bases

        elif command == "COMP":
            response = Seq.complement(arg)

        elif command == "REV":
            response = Seq.reverse(arg)

        elif command == "GENE":
            response = Seq.read_fasta2(FOLDER + arg)

        else:
            response = "Command not available in this server\n"

        print(response)
        send_bytes = str.encode(Fore.LIGHTGREEN_EX + response)
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()