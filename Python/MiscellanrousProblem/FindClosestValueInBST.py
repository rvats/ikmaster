def findClosestValueInBst(tree, target):
    valueDiff = float("inf")
    if tree is None:
        return None
    else:
        if tree.value == target:
            return tree.value
        else:
           if tree.value < target:
               valueDiff = target - tree.value
               return
           elif tree.value > target:

            


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
