import socket
import threading
import sys
import pickle
from time import sleep

choice = "||==============================||\n" \
         "    Escolha uma opção: \n" + \
         "    1 - Ler arquivo \n" + \
         "    2 - Renomear arquivo \n" + \
         "    3 - Criar arquivo \n" + \
         "    4 - Remover arquivo\n" + \
         "    Any - Finalizar Aplicação!\n" \
         "||==============================||"

print(choice)

class Cliente():
    def __init__(self, host="192.168.0.183", port=3022):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        msg_recv = threading.Thread(target=self.msg_recv)

        msg_recv.daemon = True
        msg_recv.start()

        while True:
            print("Inicializando...")
            sleep(3)
            msg = input("\nSua escolha: ")
            if msg == "1":
                nome = input("Digite o nome do arquivo que deseja ser lido: ") + ".txt"
                self.send_msg(pickle.dumps([msg, nome]))
            elif msg == "2":
                nome = input("Digite o nome do arquivo que deseja ser nomeado: ") + ".txt"
                new_nome = input("Digite seu novo nome: ") + ".txt"
                self.send_msg(pickle.dumps([msg, nome, new_nome]))
            elif msg == "3":
                nome = input("Digite o nome do arquivo que deseja ser criado: ") + ".txt"
                self.send_msg(pickle.dumps([msg, nome]))
            elif msg == "4":
                nome = input("Digite o nome do arquivo que deseja ser removido: ") + ".txt"
                self.send_msg(pickle.dumps([msg, nome]))
            else:
                print("\n--- Manipulação Finalizada ---\n")
                self.sock.close()
                sys.exit()

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print("\n||==============================||\n[*] Resultado:"
                          "\n ###\n\n"
                          + bytes.decode(data), "\n\n ### \n" + choice + "\n")
            except:
                pass

    def send_msg(self, msg):
        self.sock.send(msg)


c = Cliente()