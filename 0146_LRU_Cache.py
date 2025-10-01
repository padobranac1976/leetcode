from collections import OrderedDict


class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        self.dictionary.move_to_end(key)
        return self.dictionary[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.dictionary.move_to_end(key)

        self.dictionary[key] = value

        if len(self.dictionary) > self.capacity:
            self.dictionary.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    input1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    input2 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    output = []

    for i, command in enumerate(input1):
        if command == "LRUCache":
            obj = LRUCache(input2[i][0])
            output.append(None)
        elif command == "put":
            output.append(obj.put(input2[i][0], input2[i][1]))
        elif command == "get":
            output.append(obj.get(input2[i][0]))
    print(output)