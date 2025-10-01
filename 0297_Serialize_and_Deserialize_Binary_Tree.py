# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs1(node, string):
            if node is None:
                string += "None,"
            else:
                string += str(node.val) + ","
                string = dfs1(node.left, string)
                string = dfs1(node.right, string)
            return string

        return dfs1(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs2(string):
            if string[0] == "None":
                string.pop(0)
                return None

            node = TreeNode(string.pop(0))
            node.left = dfs2(string)
            node.right = dfs2(string)
            return node

        root = dfs2(data.split(","))
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == '__main__':
    root = TreeNode(1)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node3.left = node4
    node3.right = node5
    root.left = node2
    root.right = node3

    obj = Codec()
    print(obj.serialize(root))