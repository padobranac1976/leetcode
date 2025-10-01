import heapq


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.trie = {}
        for s, freq in zip(sentences, times):
            self.enter(s, freq)
        self.current_input = ""
        self.curr_node = self.trie

    def enter(self, sentence, frequency):
        node = self.trie
        for c in sentence:
            node = node.setdefault(c, {"frequency": {}})
            node["frequency"][sentence] = node["frequency"].get(sentence, 0) + frequency

    def input(self, c):
        if c == "#":
            self.enter(self.current_input, 1)
            self.current_input = ""
            self.curr_node = self.trie
        else:
            self.current_input += c
            if self.curr_node and c in self.curr_node:
                self.curr_node = self.curr_node[c]
                pque = [(-frequency, sentence) for sentence, frequency in self.curr_node["frequency"].items()]
                return [result[1] for result in heapq.nsmallest(3, pque)]
            else:
                self.curr_node = None
                return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


if __name__ == '__main__':
    input1 = ["AutocompleteSystem", "input", "input", "input", "input"]
    input2 = [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
    output = []

    for i, command in enumerate(input1):
        if command == "AutocompleteSystem":
            obj = AutocompleteSystem(input2[i][0], input2[i][1])
            output.append(None)
        elif command == "input":
            output.append(obj.input(input2[i][0]))
    print(output)