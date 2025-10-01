from collections import deque


class StreamChecker:
    def __init__(self, words):
        self.trie = {}
        self.stream = deque([])

        for w in set(words):
            node = self.trie

            for c in w[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]

            node["#"] = w

    def query(self, letter):
        self.stream.appendleft(letter)
        node = self.trie

        for c in self.stream:
            if "#" in node:
                return True

            if c not in node:
                return False

            node = node[c]

        return "#" in node


if __name__ == '__main__':
    input1 = ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
    input2 = [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
    output = []
    for i, inpt in enumerate(input1):
        if inpt == "StreamChecker":
            obj = StreamChecker(input2[i][0])
            output.append(None)
        else:
            output.append(obj.query(input2[i][0]))

    print(output)



