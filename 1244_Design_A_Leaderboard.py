from typing import List
import heapq

class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        self.scoreboard = []
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = score
            heapq.heappush(self.scoreboard, (-score, playerId))
            
        else:
            prev_score = self.leaderboard[playerId]
            self.leaderboard[playerId] += score

            # remove previous score
            self.scoreboard.remove((-prev_score, playerId))
            
            # add new score
            heapq.heappush(self.scoreboard, (-self.leaderboard[playerId], playerId))

    def top(self, K: int) -> int:        
        best_K = heapq.nsmallest(K, self.scoreboard)
        
        result = 0
        for score, candidate in best_K:
            result += -score
            
        return result
            

    def reset(self, playerId: int) -> None:        
        self.scoreboard.remove((-self.leaderboard[playerId], playerId))
        del self.leaderboard[playerId]
        


# Your SnakeGame object will be instantiated and called as such:
commands = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
parameters = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

output = []
for i, command in enumerate(commands):
    if command == "Leaderboard":
        obj = Leaderboard()
        output.append(None)
    elif command == "addScore":
        output.append(obj.addScore(*parameters[i]))
    
    elif command == "top":
        output.append(obj.top(parameters[i][0]))
        
    elif command == "reset":
        output.append(obj.reset(parameters[i][0]))
print(output)