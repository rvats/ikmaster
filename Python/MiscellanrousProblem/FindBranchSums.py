# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    branchSumsCollection = []
    def branchSumsHelper(root, branchSumsCollection, currentBranchSum):
        if root.left is None and root.right is None:
            branchSumsCollection.append(currentBranchSum+root.value)
        else:
            if(root.left is not None):
                branchSumsHelper(root.left,branchSumsCollection,currentBranchSum+root.value)
            if(root.right is not None):
                branchSumsHelper(root.right,branchSumsCollection,currentBranchSum+root.value)
        return branchSumsCollection
    branchSumsHelper(root,branchSumsCollection,0)
    return branchSumsCollection

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right.left = BinaryTree(10)

print(branchSums(root))