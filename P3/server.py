import socket
from colorama import init, Fore

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 6123
IP = "127.0.0.1"
seq0 = "AGAGAGAGAGAGAGA"
seq1 = "ATATATATATATATA"
seq2 = "CACACACACACACAC"
seq3 = "TGTGTGTGTGTGTGT"
seq4 = "CGCGCGCGCGCGCGC"

sequences = [seq0, seq1, seq2, seq3, seq4]

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()
    else:
        init(autoreset=True)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]


        # -- Print the received message

        if cmd != "PING":
            arg = splitted_command[1]
            print(Fore.LIGHTGREEN_EX + cmd)

        if cmd == "PING":
            response = "OK\n"
        elif cmd == "GET":
            response = sequences[int(arg)]
            print(sequences[int(arg)])
        elif cmd == "INFO":
            print("Sequence:", arg)
            print("The length:", len(arg))
            response = arg


        else:
            # -- Send a response message to the client
            response = "This comand is not available in the server\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()