# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    print(root.value, depth)
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

def nodeDepthsIterative (root): 
	sumOfDepths = 0
	stack = [{"node": root, "depth": 0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths+=depth
		stack.append({"node": node.left, "depth": depth+1})
		stack.append({"node": node.right, "depth": depth+1})
	return sumOfDepths

root = BinaryTree(1) # Depth = 0
root.left = BinaryTree(2) # Depth = 1
root.right = BinaryTree(3) # Depth = 1
root.left.left = BinaryTree(4) # Depth = 2
root.left.right = BinaryTree(5) # Depth = 2
root.right.left = BinaryTree(6) # Depth = 2
root.right.right = BinaryTree(7) # Depth = 2
root.left.left.left = BinaryTree(8)  # Depth = 3
root.left.left.right = BinaryTree(9) # Depth = 3
root.left.right.left = BinaryTree(10) # Depth = 3

print(nodeDepths(root))
