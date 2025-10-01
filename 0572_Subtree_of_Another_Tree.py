def isSubtree(root, subRoot):
    if not root:
        return False

    def isEqual(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val == tree2.val:
            return isEqual(tree1.left, tree2.left) and isEqual(tree1.right, tree2.right)

    if isEqual(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


if __name__ == '__main__':
    r = [3,4,5,1,2]
    sr = [4,1,2]
    result = isSubtree(r, sr)
    print(result)


