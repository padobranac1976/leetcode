class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    input1 = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    input2 = [[],[-2],[0],[-3],[],[],[],[]]
    output = []

    for i, command in enumerate(input1):
        if command == "MinStack":
            obj = MinStack()
            output.append(None)
        elif command == "push":
            output.append(obj.push(input2[i][0]))
        elif command == "top":
            output.append(obj.top())
        elif command == "getMin":
            output.append(obj.getMin())
        elif command == "pop":
            output.append(obj.pop())

    print(output)