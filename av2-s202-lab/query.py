from database import Database
class Question12:

    def __init__(self):
        db = Database("bolt://54.175.13.242:7687", "neo4j", "driller-clocks-barriers")
        self.db = db

    
    def findRenzo(self):
        query = """
        MATCH (t:Teacher {name: 'Renzo'})
        RETURN t.ano_nasc, t.cpf;  
        """
        return self.db.execute_query(query)
    
    def findTeacherWithM(self):
        query = """
         MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name, t.cpf;
        """
        return self.db.execute_query(query)
    def findCityName(self):
        query = """
        MATCH (c:City)
        RETURN c.name;
        """
        return self.db.execute_query(query)
    def findSchoolsBiggerThan150(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name, s.address, s.number;
        """
        return self.db.execute_query(query)
    
    def minMaxYear(self):
        query = """
        MATCH (t:Teacher)
        RETURN min(t.ano_nasc), max(t.ano_nasc);
        """
        return self.db.execute_query(query)
    
    def averageCityPopulation(self):
        query = """
        MATCH (c:City)
        RETURN avg(c.population);
        """
        return self.db.execute_query(query)
    
    def findSaintRoots(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN REPLACE(c.name, 'a', 'A') AS cityName;
        """
        return self.db.execute_query(query)
    
    def findTeachersLetters(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 3, 1) AS thirdCharacter;
         """
        return self.db.execute_query(query)

db = Database("bolt://54.175.13.242:7687", "neo4j", "driller-clocks-barriers")   
questions = Question12()


print("Encontrar o professor 'Renzo")
result = questions.findRenzo()
print(result)

print("Encontrar professores cujos nomes começam com 'M'")
result = questions.findTeacherWithM()
print(result)

print("Encontrar os nomes das cidades")
result = questions.findCityName()
print(result)

print("Encontrar escolas com número entre 150 e 550.")
result = questions.findSchoolsBiggerThan150()
print(result)


print("Encontre o ano de nascimento do professor mais jovem e do professor mais velho.")
result = questions.minMaxYear()
print(result)

print("Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade 'population'.")
result = questions.averageCityPopulation()
print(result)

print("Encontre a cidade cujo CEP seja igual a '37540-000' e retorne o nome com todas as letras 'a' substituídas por 'A'.")
result = questions.findSaintRoots()
print(result)

print("Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.")
result = questions.findTeachersLetters()
print(result)

db.close()