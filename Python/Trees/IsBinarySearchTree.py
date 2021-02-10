class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def isBST(root):
    def isBSTUtil(node, minValue, maxi): 
        if node is None: 
            return True
        if node.val < minValue or node.val > maxi: 
            return False
        return (isBSTUtil(node.left_ptr, mini, node.val) and isBSTUtil(node.right_ptr, node.val, maxi))
    return (isBSTUtil(root, float("-inf"), float("inf"))) 