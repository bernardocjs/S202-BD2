
class Family:
    def __init__(self, database):
        self.db = database

    def create_parent(self, name, sex, age):
        query = """
        CREATE (:Person {name: $name})
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_parents(self, name):
        query = """
            MATCH (p:Person {name: $name})-[:PARENT_OF]->(c:Person)
            RETURN c.name as name
        """
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)
    
    def get_brothers(self, name):
        query = """""
            MATCH (p:Person {name: $name})-[:BROTHER_OF]->(c:Person)<-[:BROTHER_OF]-(s:Person)
            WHERE p <> s
            RETURN s.name as name
        """
        return self.db.execute_query(query, {"name": name})
    
