from database import Database
database = Database("bolt://54.175.13.242:7687", "neo4j", "driller-clocks-barriers")

def seed():
    database.drop_all()
    family = [
        """
        CREATE (p:Pessoa:Psicologa {name: 'Luciana', age: 39, gender: 'F'})
        """,
        """
        CREATE (p:Pessoa:Desenvolvedor {name: 'Bernardo', age: 20, gender: 'M'})
        """,
        """
        CREATE (p:Pessoa:Atoa {name: 'Caique', age: 23, gender: 'M'})
        """,
        """
        CREATE (p:Pessoa:Desenvolvedor {name: 'Ricardo', age: 28, gender: 'M'})
        """,
        """
        CREATE (p:Pessoa:Desenvolvedor {name: 'Isabela', age: 19, gender: 'F'})
        """,
        """
        CREATE (p:Pessoa:Gerente {name: 'Marco', age: 43, gender: 'M'})
        """,
        """
        CREATE (p:Pessoa:Veterinario {name: 'Mariana', age: 20, gender: 'F'})
        """,
        """
        CREATE (p:Pet:Cachorro {name: 'Tasha', age: 3, gender: 'F'})
        """,
        """
        CREATE (p:Pet:Cat {name: 'gato', age: 1, gender: 'F'})
        """,
        """
        CREATE (p:Pet:Cat {name: 'gato Gordo', age: 1, gender: 'M'})
        """
    ]

    relations = [
        """
        MATCH (p1: Pessoa {name: 'Luciana'}), (p2: Pessoa {name: 'Bernardo'})
        CREATE (p1)-[:PAI_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Luciana'}), (p2: Pessoa {name: 'Caique'})
        CREATE (p1)-[:PAI_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Bernardo'}), (p2: Pessoa {name: 'Caique'})
        CREATE (p1)-[:IRMÃO_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Marco'}), (p2: Pessoa {name: 'Bernardo'})
        CREATE (p1)-[:PAI_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Marco'}), (p2: Pessoa {name: 'Caique'})
        CREATE (p1)-[:PAI_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Isabela'}), (p2: Pessoa {name: 'Bernardo'})
        CREATE (p1)-[:NAMORA{since: '2021'}]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Mariana'}), (p2: Pessoa {name: 'Caique'})
        CREATE (p1)-[:NAMORA]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Bernardo'}), (p2: Pet {name: 'gato'})
        CREATE (p1)-[:DONO_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Bernardo'}), (p2: Pet {name: 'gato Gordo'})
        CREATE (p1)-[:DONO_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Caique'}), (p2: Pessoa {name: 'Bernardo'})
        CREATE (p1)-[:IRMAO_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Mariana'}), (p2: Pessoa {name: 'Ricardo'})
        CREATE (p1)-[:PRIMO_DE]->(p2)
        """,
        """
        MATCH (p1: Pessoa {name: 'Caique'}), (p2: Pet {name: 'Tasha'})
        CREATE (p1)-[:DONO_DE]->(p2)
        """
    ]
    for fm in family:
        database.execute_query(fm)

    for relation in relations:
        database.execute_query(relation)
    
seed()

while True:
    print("------------------------------")
    print("1. Quais são os gatos da família?")
    print("2. Quais são os pais de Bernardo?")
    print("3. Quem é o dono de Tasha?")
    print("0. Sair")

   
    choice = input("Escolha uma opção: ")
    print("------------------------------")

    if choice == "1":
        q1 = """
        MATCH (c:Pet:Cat) RETURN c.name
        """
        cats = database.execute_query(q1)
        for cat in cats:
            print(cat[0])
        
    elif choice == "2":
        q2 = """
        MATCH (b:Pessoa {name: 'Bernardo'})<-[r:PAI_DE]-(parent)
        RETURN parent.name
        """
        parents = database.execute_query(q2)
        for parent in parents:
            print(parent[0])

    elif choice == "3":
        q3 = """
        MATCH (t:Pet {name: 'Tasha'})<-[r:DONO_DE]-(owner)
        RETURN owner.name
        """
        owners = database.execute_query(q3)
        for owner in owners:
            print(owner[0])
    elif choice == "0":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")