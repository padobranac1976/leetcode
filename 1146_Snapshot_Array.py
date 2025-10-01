class SnapshotArray:

    def __init__(self, length):
        self.snapshots = [{}]
        self.snap_id = -1

    def set(self, index, val):
        self.snapshots[-1][index] = val

    def snap(self):
        self.snapshots.append(self.snapshots[-1].copy())
        self.snap_id += 1
        return self.snap_id

    def get(self, index, snap_id):
        if index in self.snapshots[snap_id]:
            return self.snapshots[snap_id][index]
        return 0


if __name__ == '__main__':
    input1 = ["SnapshotArray","set","snap","set","get"]
    input2 = [[3],[0,5],[],[0,6],[0,0]]
    output = []
    for i, inpt in enumerate(input1):
        if inpt == "SnapshotArray":
            obj = SnapshotArray(input2[i][0])
            output.append(None)
        elif inpt == "set":
            output.append(obj.set(input2[i][0],input2[i][1]))
        elif inpt == "snap":
            output.append(obj.snap())
        elif inpt == "get":
            output.append(obj.get(input2[i][0], input2[i][1]))

    print(output)


