from collections import deque


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.q1 = deque(v1)
        self.q2 = deque(v2)
        self.pointer = 1

    def next(self) -> int:
        if self.pointer == 1:
            if self.q2:
                self.pointer = 2
            if self.q1:
                return self.q1.popleft()

        if self.pointer == 2:
            if self.q1:
                self.pointer = 1
            if self.q2:
                return self.q2.popleft()

    def hasNext(self) -> bool:
        if self.q1 or self.q2:
            return True

        return False


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    vec1 = [1,2]
    vec2 = [3,4,5,6]
    i, v = ZigzagIterator(vec1, vec2), []
    while i.hasNext(): v.append(i.next())
    print(v)