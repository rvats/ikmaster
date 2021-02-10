class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self
	
	def contains(self, value):
		if value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True
	
	def remove(self, value, parent=None):
		if value < self.value:
			if self.left is not None:
				self.left.remove(value, self)
		elif value > self.value:
			if self.right is not None:
				self.right.remove(value, self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMinValue()
				self.right.remove(self.value, self)
			elif parent is None:
				if self.left is not None:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					pass
			elif parent.left == self:
				parent.left = self.left if self.left is not None else self.right
			elif parent.right == self:
				parent.right = self.left if self.left is not None else self.right
		return self
	
	def getMinValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMinValue()

def validateBst(tree, isValidBST = True):
	def isBSTUtil(node, minValue, maxValue):
		if node is None:
			return True
		if node.value < minValue or node.value >= maxValue:
			return False
		return (isBSTUtil(node.left, minValue, node.value) and isBSTUtil(node.right, node.value, maxValue))
	return (isBSTUtil(tree, float("-inf"), float("inf")))

def inOrderTraverse(tree, array):
	if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array


def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array

def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array


bst = BST(10)
bst.left = BST(5)
bst.left.left = BST(2)
bst.left.left.left = BST(1)
bst.left.right = BST(5)
bst.right = BST(15)
bst.right.left = BST(13)
bst.right.left.right = BST(14)
bst.right.right = BST(22)
print(bst.insert(12))
print(validateBst(bst))
print(inOrderTraverse(bst,[]))
print(preOrderTraverse(bst,[]))
print(postOrderTraverse(bst,[]))
print(bst.remove(10))
print(bst.contains(14))
print(validateBst(bst))
print(inOrderTraverse(bst,[]))
print(preOrderTraverse(bst,[]))
print(postOrderTraverse(bst,[]))