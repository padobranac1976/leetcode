import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findLeaves(self, root):
    def dfs(node, layer):
        if not node:
            return layer

        left = dfs(node.left, layer)
        right = dfs(node.right, layer)
        layer = max(left, right)
        nodes[layer].append(node.val)
        return layer + 1

    nodes = collections.defaultdict(list)
    dfs(root, 0)

    return nodes.values()


if __name__ == '__main__':
    n = [1,2,3,4,5]
    result = findLeaves(n)
    print(result)


