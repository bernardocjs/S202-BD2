database = Database("neo4j://localhost:7687", "your_username", "your_password")

family = """
    CREATE (p:Pessoa :Psicologa {name: 'Luciana', age: 39, gender: 'F'})
    CREATE (p:Pessoa :Desenvolvedor {name: 'Bernardo', age: 20, gender: 'M'})
    CREATE (p:Pessoa :Atoa {name: 'Caique', age: 23, gender: 'M'})
    CREATE (p:Pessoa :Desenvolvedor {name: 'Ricardo', age: 28, gender: 'M'})
    CREATE (p:Pessoa :Desenvolvedor {name: 'Isabela', age: 19, gender: 'F'})
    CREATE (p:Pessoa :Gerente {name: 'Marco', age: 43, gender: 'M'})
    CREATE (p:Pessoa :Veterinario {name: 'Mariana', age: 20, gender: 'F'})
    CREATE (p:Pet :Cachorro {name: 'Tasha', age: 3, gender: 'F'})
    CREATE (p:Pet :Cat {name: 'gato', age: 1, gender: 'F'})
    CREATE (p:Pet :Cat {name: 'gato Gordo', age: 1, gender: 'M'})
"""

database.execute_query(family)

relation = """
MATCH(p1: Pessoa {name: 'Luciana'}), (p2: Pessoa {name: 'Bernardo'})
CREATE (p1)-[:PAI_DE]->(p2)

MATCH (p1:Pessoa {name: 'Luciana'}), (p2:Pessoa {name: 'Caique'})
CREATE (p1)-[:PAI_DE]->(p2)

MATCH (p1:Pessoa {name: 'Bernardo'}), (p2:Pessoa {name: 'Caique'})
CREATE (p1)-[:IRMÃO_DE]->(p2)

MATCH (p1:Pessoa {name: 'Marco'}), (p2:Pessoa {name: 'Bernardo'})
CREATE (p1)-[:PAI_DE]->(p2)

MATCH (p1:Pessoa {name: 'Marco'}), (p2:Pessoa {name: 'Caique'})
CREATE (p1)-[:PAI_DE]->(p2)

MATCH (p1:Pessoa {name: 'Isabela'}), (p2:Pessoa {name: 'Bernardo'})
CREATE (p1)-[:NAMORA]->(p2)

MATCH (p1:Pessoa {name: 'Mariana'}), (p2:Pessoa {name: 'Caique'})
CREATE (p1)-[:NAMORA]->(p2)

MATCH (p1:Pessoa {name: 'Bernardo'}), (p2:Pet {name: 'gato'})
CREATE (p1)-[:DONO_DE]->(p2)

MATCH (p1:Pessoa {name: 'Bernardo'}), (p2:Pet {name: 'gato Gordo'})
CREATE (p1)-[:DONO_DE]->(p2)

MATCH (p1:Pessoa {name: 'Caique'}), (p2:Pessoa {name: 'Bernardo'})
CREATE (p1)-[:IRMAO_DE]->(p2)

MATCH (p1:Pessoa {name: 'Mariana'}), (p2:Pessoa {name: 'Ricardo'})
CREATE (p1)-[:PRIMO_DE]->(p2)

MATCH (p1:Pessoa {name: 'Caique'}), (p2:Pet {name: 'Tasha'})
CREATE (p1)-[:DONO_DE]->(p2)
"""

database.execute_query(relation)

# 1. Quais são os gatos da familia?
q1 = """
MATCH (c:Pet:Cat) RETURN c
"""
database.execute_query(q1)

# 2. Quais são os pais de Bernardo?
q2 = """
MATCH (b:Pessoa {name: 'Bernardo'})<-[r:PAI_DE]-(parent)
RETURN parent
"""

database.execute_query(q2)

# 3. Quem é o dono de Tasha?
q3 = """
MATCH (t:Pet {name: 'Tasha'})<-[r:DONO_DE]-(owner)
RETURN owner
"""