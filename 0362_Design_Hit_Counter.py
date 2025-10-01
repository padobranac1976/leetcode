class HitCounter:

    def __init__(self):
        self.sliding_window = 300
        self.hits = {}
        self.accumulated_hits = 0
        
    def hit(self, timestamp: int) -> None:
        if timestamp not in self.hits:
            self.hits[timestamp] = 0
        self.hits[timestamp] += 1
        self.accumulated_hits += 1

    def getHits(self, timestamp: int) -> int:
        all_ts = list(self.hits.keys())
        for t in all_ts:
            if timestamp - t >= self.sliding_window:                
                self.accumulated_hits -= self.hits[t]
                self.hits.pop(t)
            else:
                break
        return self.accumulated_hits

if __name__ == '__main__':
    input1 = ["HitCounter","hit","hit","hit","hit","hit","hit","getHits","hit","getHits","hit","getHits"]
    input2 = [[],[100],[282],[411],[609],[620],[744],[879],[956],[976],[998],[1055]]
    output = []
    for i, inpt in enumerate(input1):
        if inpt == "HitCounter":
            obj = HitCounter()
            output.append(None)
        elif inpt == "hit":
            result = obj.hit(input2[i][0])
            output.append(result)
        else:
            result = obj.getHits(input2[i][0])
            output.append(result)

    print(output)



