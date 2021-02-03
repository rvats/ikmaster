# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
    nodeDepthsSum, currentNodeDepth = 0, 0
    def nodeDepthsSumHelper(root, currentNodeDepth, nodeDepthsSum):
        if root.left is None and root.right is None:
            nodeDepthsSum = nodeDepthsSum + currentNodeDepth
            print(root.value, currentNodeDepth, nodeDepthsSum)
            return nodeDepthsSum
        else:
            if(root.left is not None):
                nodeDepthsSum = nodeDepthsSumHelper(root.left,currentNodeDepth+1,nodeDepthsSum + currentNodeDepth)
                print(root.value, currentNodeDepth, nodeDepthsSum)
            if(root.right is not None):
                nodeDepthsSum = nodeDepthsSumHelper(root.right,currentNodeDepth+1,nodeDepthsSum + currentNodeDepth)
                print(root.value, currentNodeDepth, nodeDepthsSum)
        return nodeDepthsSum
    nodeDepthsSum = nodeDepthsSumHelper(root,0,0)
    print(root.value, currentNodeDepth, nodeDepthsSum)
    return nodeDepthsSum

root = BinaryTree(1) # Depth = 0
root.left = BinaryTree(2) # Depth = 1
root.right = BinaryTree(3) # Depth = 1
root.left.left = BinaryTree(4) # Depth = 2
root.left.right = BinaryTree(5) # Depth = 2
#root.right.left = BinaryTree(6) # Depth = 2
#root.right.right = BinaryTree(7) # Depth = 2
#root.left.left.left = BinaryTree(8)  # Depth = 3
#root.left.left.right = BinaryTree(9) # Depth = 3
#root.left.right.left = BinaryTree(10) # Depth = 3

print(nodeDepths(root))
