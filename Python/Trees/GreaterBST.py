# == == == == == == == == == == == == == == == == == == == == == =
#
# Given the root of a Binary Search Tree (BST),
# "convert" it to a Greater Tree such that every key of the original BST is
# changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example 1:
#
# Input: TreeNode(4)
#             4
#           /   \
#          1      6
#        /  \    / \
#       0    2   5   7
#             \       \
#              3       8
# Output: void
#             30
#           /   \
#          36     21
#        /  \    / \
#       36  35  26   15
#             \       \
#             33       8
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# 0 <= TreeNode.val <= 100
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
#
# == == == == == == == == == == == == == == == == == == == == == =

def greaterBinarySearchTree(treeNode):
