import random


class RandomizedSet:

    def __init__(self):
        self.myDict = {}
        self.myList = []

    def insert(self, val: int) -> bool:
        if val in self.myDict:
            return False

        self.myDict[val] = len(self.myList)
        self.myList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.myDict:
            return False

        last = self.myList[-1]
        idx = self.myDict[val]
        self.myList[idx] = last
        self.myDict[last] = idx
        self.myList.pop()
        del self.myDict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.myList)


if __name__ == '__main__':
    input1 = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    input2 = [[], [1], [2], [2], [], [1], [2], []]
    output = []

    for i, command in enumerate(input1):
        if command == "RandomizedSet":
            obj = RandomizedSet()
            output.append(None)
        elif command == "insert":
            output.append(obj.insert(input2[i][0]))
        elif command == "remove":
            output.append(obj.remove(input2[i][0]))
        elif command == "getRandom":
            output.append(obj.getRandom())
    print(output)