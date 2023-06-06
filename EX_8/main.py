from database import Database
from crud import Game
db = Database("bolt://54.175.13.242:7687", "neo4j", "driller-clocks-barriers")
game = Game(db)

game.createPlayer("Player 1", 1)
game.createPlayer("Player 2", 2)
players = game.getPlayers()
print("Players:")
for player in players:
    print(player["name"], player["id"])

game.updatePlayer("Player 1", "New Name")
game.deletePlayer(2)

game.createMatch("Match 1", "Win", [{"Player 1": 100}, {"Player 2": 80}])
game.createMatch("Match 2", "Loss", [{"Player 1": 50}, {"Player 2": 70}])
matches = game.getMatches()
print("Matches:")
for match in matches:
    print(match["name"], match["result"])

game.createRelationship("Player 1", "Player 2")

player_history = game.getPlayerHistory("Player 1")
print("Player 1 History:")
for history in player_history:
    print(history["match_name"], history["match_result"], history["player_score"])

game.deleteMatch("Match 2")