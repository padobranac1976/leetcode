# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # 1st find paths from root to both the nodes

        fp, sp = [], []
        self.call(root, fp, startValue)  # gives the path from root to 1st node
        self.call(root, sp, destValue)  # gives the path from root to 2nd node

        while fp and sp and fp[-1] == sp[-1]:  # ** Remove the nodeswhich are common in both paths .**
            fp.pop()
            sp.pop()
        return 'U' * (len(fp)) + ''.join(reversed(sp))

    def call(self, root, path, val):
        # if not root:
        #    return False
        if root.val == val:
            return True

        if root.left:
            # arr.append('L')
            if self.call(root.left, path, val):
                path.append('L')
                return True
                # path.pop()

        if root.right:
            # arr.append('L')
            if self.call(root.right, path, val):
                path.append('R')
                return True
                # path.pop()
