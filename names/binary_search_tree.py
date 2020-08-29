"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Self is equal to the root = Everything is compared to self
        # Steps
        # Create the new node being inserted
        newNode = BSTNode(value)
        # Compare the node to the root
        # if Greater compare to roots right value
        if newNode.value >= self.value:
            # If root Right value is None - Place Node
            if self.right == None:
                self.right = newNode
            # Else root.right.insert(NewNode) - Run recursion
            else:
                return self.right.insert(value)
        # else Lesser compare to the roots left value
        else:
            if self.left == None:
                self.left = newNode
            # If root Left value is None - Place Node
            else:
                return self.left.insert(value)
            # Else root.left.insert(NewNode) - Run recursion

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Steps
        # Compare value to Root
        if target == self.value:
            return True
        # If Greater check Right
        if target > self.value:
            # if right is none return False
            if self.right == None:
                return False
            # elif right == target return true
            elif self.right.value == target:
                return True
            # else Run Recursion
            else:
                return self.right.contains(target)
        # Else Check Left
        else:
            # If None Return False
            if self.left == None:
                return False
            # elif left == target return true
            elif self.left.value == target:
                return True
            # else Run Recursion
            else:
                return self.left.contains(target)
