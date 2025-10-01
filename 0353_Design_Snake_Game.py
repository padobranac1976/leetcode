from typing import List
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):        
        self.head_r = 0
        self.head_c = 0
        self.prev_row = 0
        self.prev_col = 0
        self.tail = []
        self.score = 0
        self.width = width
        self.height = height
        self.food = food       
        self.directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
        
    def move(self, direction: str) -> int:
        self.prev_row = self.head_r
        self.prev_col = self.head_c
        
        self.head_r += self.directions[direction][0]
        self.head_c += self.directions[direction][1]
        
        if self.food and self.food[0] == [self.head_r, self.head_c]:
            self.score += 1
            self.tail.append((self.prev_row, self.prev_col))
            self.food.pop(0)
        else:            
            self.tail.append((self.prev_row, self.prev_col))
            self.tail.pop(0)
        
        if (self.head_r, self.head_c) in self.tail \
                or self.head_c < 0 or self.head_c == self.width \
                or self.head_r < 0 or self.head_r == self.height:
            return -1
        
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
		
commands = ["SnakeGame","move","move","move","move","move","move"]
parameters = [[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]
expected_output = [None,0,0,1,1,2,-1]

output = []
for i, command in enumerate(commands):
	if command == "SnakeGame":
		obj = SnakeGame(parameters[i][0], parameters[i][1], parameters[i][2])
		output.append(None)      
	else:
		result = obj.move(parameters[i][0])
		output.append(result)

print(output)
