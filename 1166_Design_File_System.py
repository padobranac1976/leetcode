from collections import defaultdict

class TrieNode(object):
  def __init__(self, name):
    self.paths = defaultdict(TrieNode)
    self.name = name
    self.value = -1

class FileSystem:
    def __init__(self):
      self.root = TrieNode("")        

    def createPath(self, path: str, value: int) -> bool:      
      parts = path.split("/")
      node = self.root
      
      for i in range(1, len(parts)):
        name = parts[i]
        if name not in node.paths:
          if i == len(parts) - 1:
            node.paths[name] = TrieNode(name)
          else:
            return False
        node = node.paths[name]
      
      if node.value != -1:
        return False
    
      node.value = value
      return True
        
    def get(self, path):
      node = self.root
      parts = path.split("/")
      for i in range(1, len(parts)):
        name = parts[i]
        if name not in node.paths:
          return -1
        node = node.paths[name]
      return node.value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

if __name__ == '__main__':
    input1 = ["FileSystem","createPath","createPath","get","createPath","get"]
    input2 = [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
    output = []
    for i, inpt in enumerate(input1):
        if inpt == "FileSystem":
            obj = FileSystem()
            output.append(None)
        elif inpt == "createPath":
            result = obj.createPath(input2[i][0], input2[i][1])
            output.append(result)
        else:
            result = obj.get(input2[i][0])
            output.append(result)

    print(output)



