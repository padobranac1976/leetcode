import bisect

class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        self.score = {}
        self.times = times
        self.leader = []
        self.max = 0
        
        for vote in persons:
            if vote not in self.score:
                self.score[vote] = 0
            self.score[vote] += 1
            
            if self.score[vote] >= self.max:
                self.leader.append(vote)
                self.max = self.score[vote]
            else:
                self.leader.append(self.leader[-1])
            

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.times, t)
        return self.leader[i-1]
		
commands = ["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"]
parameters = [[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]
expected_output = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

output = []
for i, command in enumerate(commands):
	if command == "TopVotedCandidate":
		obj = TopVotedCandidate(parameters[i][0], parameters[i][1])
		output.append(None)      
	else:
		result = obj.q(parameters[i][0])
		output.append(result)

print(output)		
assert output == expected_output
