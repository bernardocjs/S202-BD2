import pymongo  # pip install pymongo


class Database:

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString, tlsAllowInvalidCertificates=True)
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
            return self.db[collection]
        except Exception as e:
            print(e)