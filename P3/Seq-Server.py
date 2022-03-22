import socket
from colorama import init, Fore
from Seq1 import Seq

PORT = 7457
IP = "127.0.0.1"

seq1 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
seq2 = "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA"
seq3 = "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT"
seq4 = "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA"
seq0 = "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"

sequences = (seq0, seq1, seq2, seq3, seq4)
BASES = ["A", "C", "T", "G"]
FOLDER = "../P0/P0/sequences/U5"

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
            print("GET command!".format(Fore.LIGHTYELLOW_EX))
            if 0 <= int(arg) <= 4:
                response = sequences[int(arg)]
            else:
                response = "Argument must be an int between 0 and 4"

        elif command == "INFO":
            length = str(Seq.len(arg))
            for base in BASES:
                info = Seq.count_base(arg, base)
                bases = base + ": " + str(info[0]) + "(" + str(info[1]) + "%) \n"
            response = length + "\n" + bases

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
        serversocket.close()

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind((IP, PORT))
        serversocket.listen()
        print("Waiting for clients...")

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()