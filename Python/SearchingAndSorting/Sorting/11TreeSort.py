"""
This module creates a Binary Sort Tree ascendingly using In Order Tree Traverse;
Stable Sort;
Worst Case Time Complexity (For if the tree would be a chain Tree): O(N^2)
Average Case Time Complexity: O(N^Log N)
Memory Complexity: Not in place O(N)
"""

import random
from typing import List, TypeVar

T = TypeVar('T')

class Sorting:
    # Tree sort is a sorting algorithm that is based on Binary Search Tree data structure. It first creates a binary search tree from the elements of the input list or array and then performs an in-order traversal on the created binary search tree to get the elements in sorted order.
    # Algorithm:
    # Step 1: Take the elements input in an array.
    # Step 2: Create a Binary search tree by inserting data items from the array into the binary search tree.
    # Step 3: Perform in-order traversal on the tree to get the elements in sorted order.
    def treeSort(self, numbers):
        tree = BinarySearchTree()
        for number in numbers:
            tree.insert(number)
        tree.inorder()
        # numbers = tree.inorder()
        # return numbers

# Not sure how to design and handle the exceptions here yet
class ExceptionHandling(Exception):
    pass


class Node(object):
    def __init__(self, node_value: int) -> None:
        """
        Initializes a node with three attributes;
        `node_value` (Node Value): Must be an integer/float;
        `right_child` (Right Child): Initializes to `None`; Its value must be larger than the Root Node;
        `left_child` (Left Child): Initializes to `None`; Its value must be smaller than the Root Node;
        """
        self.node_value = node_value
        self.right_child = None
        self.left_child = None


class BinarySearchTree(object):
    def __init__(self) -> None:
        """
        Initializes the Root Node of the Binary Tree to None;
        """
        self.root = None

    def is_empty(self) -> bool:
        """
        Returns True if the tree doesn't have a node;
        """
        return self.root == None

    def insert(self, new_node: int) -> None:
        """
        Inserts an integer-value Node in the Tree;
        """
        self.root = self._insert(self.root, new_node)

    def _insert(self, parent: int, new_node: int) -> int:
        """
        Inserts an integer value in the left or right Node; 
        Returns the parent Node;
        """
        # If tree is empty
        if parent is None:
            parent = Node(new_node)
        # If the new Node value is smaller than its parent Node value
        elif new_node < parent.node_value:
            parent.left_child = self._insert(parent.left_child, new_node)
        # If the new Node value is bigger than its parent Node value
        else:
            parent.right_child = self._insert(parent.right_child, new_node)

        return parent

    def inorder(self) -> None:
        """
        Calls the _inorder traversing method;
        """
        # return self._inorder(self.root)
        self._inorder(self.root)

    def _inorder(self, parent: int) -> None:
        """
        Traverses the tree inorder (Left Node, Root Node, Right Node)
        """
        # inorderList = []
        if parent is None:
            return
        self._inorder(parent.left_child)
        # inorderList.append(parent.node_value)
        print(f'{parent.node_value}')
        self._inorder(parent.right_child)
        # return inorderList


if __name__ == '__main__':
    print("Tree Sort Demo")
    numbers = []
    for _ in range(10):
        n = random.randint(0,100) # whatever your range of random numbers is
        numbers.append(n)
    print("Numbers before Sorting: ")
    print(numbers)
    print("Numbers after Sorting: ")
    Sorting().treeSort(numbers)
    # print(Sorting().treeSort(numbers))