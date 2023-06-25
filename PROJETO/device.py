class Device:
    def __init__(self, db):
        self.db = db

    def create(self, cpf, name, mac):
        query = """
        MATCH (u:User)
        WHERE u.cpf = $cpf
        CREATE (d:Device {name: $name, mac: $mac})
        CREATE (u)-[:OWNS]->(d)
        RETURN d
        """
        parameters = {
            'cpf': cpf,
            'name': name,
            'mac': mac
        }
        return self.db.execute_query(query, parameters)

    def get(self, mac):
        query = """
        MATCH (d:Device)
        WHERE d.mac = $mac
        RETURN d
        """
        parameters = {
            'mac': mac
        }
        return self.db.execute_query(query, parameters)

    def update(self, mac, name=None):
        query = """
        MATCH (d:Device)
        WHERE d.mac = $mac
        SET d.name = coalesce($name, d.name),
            d.mac = coalesce($mac, d.mac)
        RETURN d
        """
        parameters = {
            'mac': mac,
            'name': name,
        }
        return self.db.execute_query(query, parameters)

    def delete(self, mac):
        query = """
        MATCH (d:Device)
        WHERE d.mac = $mac
        DELETE d
        """
        parameters = {
            'mac': mac
        }
        return self.db.execute_query(query, parameters)
    
    def share_device_between_users(self, device_id, owner_cpf, target_cpf):
        query = """
        MATCH (d:Device)
        WHERE d.mac = $device_id
        MATCH (owner:User)
        WHERE owner.cpf = $owner_cpf
        MATCH (target:User)
        WHERE target.cpf = $target_cpf
        CREATE (target)-[:SHARED_WTH]->(d)<-[:SHARES]-(owner)
        RETURN d
        """    
        parameters = {
            'device_id': device_id,
            'owner_cpf': owner_cpf,
            'target_cpf': target_cpf
        }
        return self.db.execute_query(query, parameters)

    def get_shared_devices(self, cpf):
        query = """
        MATCH (u:User)
        WHERE u.cpf = $cpf
        MATCH (u)-[:SHARED_WTH]->(d:Device)
        RETURN d
        """
        parameters = {
            'cpf': cpf
        }
        return self.db.execute_query(query, parameters)
    
    def get_devices_from_user(self, cpf):
        query = """
        MATCH (u:User {cpf: $cpf})-[:OWNS]->(d:Device)
        RETURN d
        UNION
        MATCH (u:User {cpf: $cpf})-[:SHARES]->(d:Device)
        RETURN d
        UNION
        MATCH (u)-[:SHARED_WTH]->(d:Device)
        RETURN d
        """
        parameters = {
            'cpf': cpf
        }
        return self.db.execute_query(query, parameters)