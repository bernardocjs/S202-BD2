class Game:
    def __init__(self, database):
        self.db = database

    def createPlayer(self, name, id):
        query = "CREATE (:Player {name: $name, id: $id})"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)

    def getPlayers(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.id AS id"
        results = self.db.execute_query(query)
        return results
    
    def updatePlayer(self, player_name, new_id):
        query = "MATCH (p:Player {name: $player_name}) SET p.name = $new_name"
        parameters = {"player_name": player_name, "new_name": new_id}
        self.db.execute_query(query, parameters)

    def deletePlayer(self, id):
        query = "MATCH (p:Player {name: $player_name}) DETACH DELETE p"
        parameters = {"player_name": id}
        self.db.execute_query(query, parameters)
        print(f"Player {id} deleted")

    def createMatch(self, match_name, match_result, match_scores):
        score_list = []
        for score in match_scores:
            player_name, player_score = next(iter(score.items()))
            score_dict = {"player_name": str(player_name), "score": int(player_score)}
            score_list.append(score_dict)

        query1 = "CREATE (:Match {name: $match_name, result: $match_result})"
        param1 = {"match_name": match_name, "match_result": match_result}
        self.db.execute_query(query1, param1)

        query2 = """
        UNWIND $score_list AS score
        MATCH (p:Player {name: score.player_name})
        MATCH (m:Match {name: $match_name})
        CREATE (p)-[:PLAYED_IN {score: score.score}]->(m)
        """
        param2 = {"match_name": match_name, "score_list": score_list}
        self.db.execute_query(query2, param2)

    def createRelationship(self, p1_id, p2_id):
        query = """
        MATCH (p1:Player {name: $p1_id})
        MATCH (p2:Player {name: $p2_id})
        CREATE (p1)-[:FRIENDS_WITH]->(p2)
        """
        parameters = {"p1_id": p1_id, "p2_id": p2_id}
        self.db.execute_query(query, parameters)


    def getPlayerHistory(self, id):
        query = """
        MATCH (p:Player {name: $player_name})-[ps:PLAYED_IN]->(m:Match)
        RETURN m.name AS match_name, m.result AS match_result, ps.score AS player_score
        """
        parameters = {"player_name": id}
        results = self.db.execute_query(query, parameters)
        return results

    def getMatches(self):
        query = "MATCH (m:Match) RETURN m.name AS name, m.result AS result"
        results = self.db.execute_query(query)
        return results

    def deleteMatch(self, match_name):
        query = "MATCH (m:Match {name: $match_name}) DETACH DELETE m"
        parameters = {"match_name": match_name}
        self.db.execute_query(query, parameters)
        print(f"Match {match_name} deleted")