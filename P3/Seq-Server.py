import socket
from colorama import init, Fore

PORT = 8020
IP = "127.0.0.1"

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
        slices = msg.split(" ")
        command = slices[0]

        if command == "PING":
            print("PING command!".format(Fore.LIGHTGREEN_EX))
            response = f"OK!\n"
            print(response)

        elif command == "GET":
            response = "none"

        send_bytes = str.encode(Fore.LIGHTGREEN_EX + response)
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()