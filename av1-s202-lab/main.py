from corridas import *
from DAO import MotoristaDAO
from cli import MotoristaCLI

# # Create a new passageiro
# passageiro = Passageiro("João", "123.456.789-10")
# print(passageiro.nome)

# # Create a new corrida
# corrida = Corrida(5, 10, 20, passageiro)
# print(corrida.distancia)

# # Create a new motorista
# motorista = Motorista(2, [corrida])
dao = MotoristaDAO()
# motoristaId = dao.create(motorista)

# # Read a motorista
# motorista = dao.read(motoristaId)
# print(motorista.nota)

# # Update a motorista
# fields = {"nota": 3}
# dao.update(motoristaId, fields)

# # Delete a motorista
# #dao.delete("123.456.789-00")

motoristaCLI = MotoristaCLI(dao)
motoristaCLI.run()
