# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_hash = {}
        output = []

        def look_in_trees(node, tree_hash, output):
            if not node:
                return -1

            left = look_in_trees(node.left, tree_hash, output)
            right = look_in_trees(node.right, tree_hash, output)

            key = (node.val, left, right)
            if key in tree_hash:
                if tree_hash[key] == 1:
                    output.append(node)
                tree_hash[key] += 1

            else:
                tree_hash[key] = 1

            return key

        look_in_trees(root, tree_hash, output)
        return output