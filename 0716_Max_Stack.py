class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        new_stack = []
        maximum = self.peekMax()
        while self.top() != maximum:
            new_stack.append(self.pop())

        self.stack.pop()

        for e in reversed(new_stack):
            self.push(e)
        return maximum


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

if __name__ == '__main__':
    input1 = ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
    input2 = [[], [5], [1], [5], [], [], [], [], [], []]
    output = []

    for i, command in enumerate(input1):
        if command == "MaxStack":
            obj = MaxStack()
            output.append(None)
        elif command == "push":
            output.append(obj.push(input2[i][0]))
        elif command == "top":
            output.append(obj.top())
        elif command == "popMax":
            output.append(obj.popMax())
        elif command == "peekMax":
            output.append(obj.peekMax())
        elif command == "pop":
            output.append(obj.pop())

    print(output)