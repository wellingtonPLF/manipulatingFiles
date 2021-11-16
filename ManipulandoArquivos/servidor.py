import socket
import threading
import sys
import pickle
from fileFunctions import fileManipulation

class Servidor():

    def __init__(self, host="192.168.0.183", port=3022):

        self.clientes = []
        self.manipularArquivo = fileManipulation()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(2)
        self.sock.setblocking(False)

        concordar = threading.Thread(target=self.aceitar)
        processar = threading.Thread(target=self.processando)

        concordar.daemon = True
        concordar.start()

        processar.daemon = True
        processar.start()

        while True:
            msg = input("[*]")
            if msg == "sair":
                self.sock.close()
                sys.exit()
            else:
                pass

    def aceitar(self):
        while True:
            try:
                cnx, addr = self.sock.accept()
                cnx.setblocking(False)
                self.clientes.append(cnx)
            except:
                pass

    def processando(self):
        print("Processando inciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        print(pickle.loads(data))
                        if data:
                            response = pickle.loads(data);
                            if(response[0] == "1"):
                                show = self.manipularArquivo.readFile(response[1])
                                c.send(str.encode(show))
                            elif (response[0] == "2"):
                                self.manipularArquivo.renameFile(response[1], response[2])
                                c.send(str.encode("Feito!"))
                            elif (response[0] == "3"):
                                self.manipularArquivo.createFile(response[1])
                                c.send(str.encode("Feito!"))
                            elif (response[0] == "4"):
                                self.manipularArquivo.removeFile(response[1])
                                c.send(str.encode("Feito!"))
                    except:
                        pass

s = Servidor()