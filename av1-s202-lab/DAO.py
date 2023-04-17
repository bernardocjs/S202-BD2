from corridas import *
from typing import Dict, Any
from database import Database
from bson.objectid import ObjectId


class MotoristaDAO:

    def __init__(self):
        self.db = Database("motorista_db", "motoristas")

    def create(self, motorista: Motorista):
        try:
            data = self.__serialize_motorista(motorista)
            motoristaCriado = self.db.collection.insert_one(data)
            print("Motorista criado com sucesso!")
            return motoristaCriado.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro durante a criacao: {e}")
            return None

    def read(self, id: str) -> Motorista:
        try:
            data = self.db.collection.find_one({"_id": ObjectId(id)})
            if data is None:
                return None
            return self.__deserialize_motorista(data)
        except Exception as e:
            print(f"Ocorreu um erro durante a leitura: {e}")
            return None

    def update(self, id: str, fields: Dict[str, Any]):
        try:
            motoristaAtualizado = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": fields})
            print("Motorista atualizado com sucesso!")
            return motoristaAtualizado
        except Exception as e:
            print(f"Ocorreu um erro durante a atualizacao: {e}")
            return None

    def delete(self, id: str):
        try:
            self.db.collection.delete_one({"_id": ObjectId(id)})
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro durante a delecao: {e}")

    def __serialize_motorista(self, motorista: Motorista):
        corridas_data = [
            self.__serialize_corrida(corrida) for corrida in motorista.corridas
        ]
        return {"nota": motorista.nota, "corridas": corridas_data}

    def __deserialize_motorista(self, data: Dict[str, Any]):
        corridas_data = data["corridas"]
        corridas = [
            self.__deserialize_corrida(cdata) for cdata in corridas_data
        ]
        return Motorista(data["nota"], corridas)

    def __serialize_corrida(self, corrida: Corrida):
        passageiro_data = {
            "nome": corrida.passageiro.nome,
            "documento": corrida.passageiro.documento
        }
        return {
            "nota": corrida.nota,
            "distancia": corrida.distancia,
            "valor": corrida.valor,
            "passageiro": passageiro_data
        }

    def __deserialize_corrida(self, data: Dict[str, Any]):
        passageiro_data = data["passageiro"]
        passageiro = Passageiro(passageiro_data["nome"],
                                passageiro_data["documento"])
        return Corrida(data["nota"], data["distancia"], data["valor"],
                       passageiro)
