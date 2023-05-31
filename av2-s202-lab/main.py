from database import Database
from teacher_crud import TeacherCRUD

class CLI:
    def __init__(self):
        db = Database("bolt://54.175.13.242:7687", "neo4j", "driller-clocks-barriers")
        self.teacher_crud = TeacherCRUD(db)

    def run(self):
        while True:
            print("--- Menu ---")
            print("1. Criar Teacher")
            print("2. Pesquisar Teacher por name")
            print("3. Atualizar CPF de um Teacher")
            print("4. Deletar Teacher")
            print("0. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.create_teacher()
            elif choice == "2":
                self.search_teacher()
            elif choice == "3":
                self.update_teacher()
            elif choice == "4":
                self.delete_teacher()
            elif choice == "0":
                break
            else:
                print("Opção inválida!")

    def create_teacher(self):
        print("-- Criar Teacher --")
        name = input("Nome: ")
        ano_nasc = int(input("Ano de Nascimento: "))
        cpf = input("CPF: ")

        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Teacher criado com sucesso!")

    def search_teacher(self):
        print("-- Pesquisar Teacher por name --")
        name = input("Nome: ")

        teacher = self.teacher_crud.read(name)
        if teacher:
            print("Teacher encontrado:")
            print(teacher)
        else:
            print("Teacher não encontrado.")

    def update_teacher(self):
        print("-- Atualizar CPF de um Teacher --")
        name = input("Nome: ")
        new_cpf = input("Novo CPF: ")

        self.teacher_crud.update(name, new_cpf)
        print("CPF atualizado com sucesso!")

    def delete_teacher(self):
        print("-- Deletar Teacher --")
        name = input("Nome: ")

        self.teacher_crud.delete(name)
        print("Teacher deletado com sucesso!")


cli = CLI()
cli.run()

