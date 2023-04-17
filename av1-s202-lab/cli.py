from DAO import MotoristaDAO
from corridas import *


class SimpleCLI:

    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com os comandos: ")
            if command == "quit":
                print("Adios!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente")


class MotoristaCLI(SimpleCLI):

    def __init__(self, motorista_dao: MotoristaDAO):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nomePassageiro = input("Entre com o nome do passageiro: ")
        documentoPassageiro = input("Entre com o documento do passageiro: ")
        passageiro = Passageiro(nomePassageiro, documentoPassageiro)
        distancia = int(input("Entre com a distancia: "))
        valor = int(input("Entre com o valor: "))
        nota = int(input("Entre com a nota da viagem: "))
        corrida = Corrida(nota, distancia, valor, passageiro)
        corridas = [corrida]
        nota = int(input("Entre com a nota do motorista: "))
        motorista = Motorista(nota, corridas)
        self.motorista_dao.create(motorista)

    def read_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_dao.read(id)
        if motorista:
            print(f"nota: {motorista['nota']}")
            print(f"corridas: {motorista['corridas']}")

    def update_motorista(self):
        nomePassageiro = input("Entre com o nome do passageiro: ")
        DocumentoPassageiro = input("Entre com o documento do passageiro: ")
        passageiro = Passageiro(nomePassageiro, DocumentoPassageiro)
        distancia = int(input("Entre com a distancia: "))
        valor = int(input("Entre com o valor: "))
        nota_corrida = int(input("Entre com a nota: "))
        corrida = Corrida(nota_corrida, distancia, valor, passageiro)
        id = input("Entre com o id: ")
        corridas = [corrida]
        nota = int(input("Enter the new nota: "))
        self.motorista_dao.update(id, corridas, nota)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_dao.delete(id)

    def run(self):
        print("Bem vindo ao app CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()