class User:
    def __init__(self, db):
        self.db = db

    def create(self, name, email, password, cpf):
        query = """
        CREATE (u:User {name: $name, email: $email, password: $password, cpf: $cpf})
        RETURN u
        """
        parameters = {
            'name': name,
            'email': email,
            'password': password,
            'cpf': cpf
        }
        return self.db.execute_query(query, parameters)

    def get(self, cpf):
        query = """
        MATCH (u:User)
        WHERE u.cpf = $cpf
        RETURN u
        """
        parameters = {
            'cpf': cpf
        }
        return self.db.execute_query(query, parameters)
    
    def get_user_by_email(self, email):
        query = """
        MATCH (u:User {email: $email})
        RETURN u
        """
        parameters = {
            'email': email
        }
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]['u']
        else:
            return None

    def update(self, cpf, name=None, email=None, password=None):
        query = """
        MATCH (u:User)
        WHERE u.cpf = $cpf
        SET u.name = coalesce($name, u.name),
            u.email = coalesce($email, u.email),
            u.password = coalesce($password, u.password)
        RETURN u
        """
        parameters = {
            'cpf': cpf,
            'name': name,
            'email': email,
            'password': password
        }
        return self.db.execute_query(query, parameters)

    def delete(self, cpf):
        query = """
        MATCH (u:User)
        WHERE u.cpf = $cpf
        DELETE u
        """
        parameters = {
            'cpf': cpf
        }
        return self.db.execute_query(query, parameters)