import socket
class Client:

    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT

    def seq_ping(self):
        print("OK!")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response


    def debug_talk(self, msg):
        import termcolor
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        msg_bytes = str.encode(msg)
        s.send(msg_bytes)
        response = s.recv(2048).decode("utf-8")
        termcolor.cprint(response, "green")

        s.close()
        return response




