# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 4/23/2026

# You may comment out the calls to the test_xxx() functions AT THE BOTTOM
# to reduce the amount printed to the screen as you work.
# Uncomment them when you are ready to test.

class TreeNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.key}, {self.value})"


class TreeMap:
    """
    The TreeMap data type implements the Map ADT (like a Python dictionary), e.g., tree[850123456]='Mike'
    The data structure is a binary search tree. Each node in the tree (a TreeNode) contains a key and a value.
    The keys are used to organize the tree. Examine the TreeNode's keys when inserting, searching, deleting, etc.,
    The values in each TreeNode are the data associated with the keys.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        """
        :return: the number of nodes in the TreeMap. This algorithm must have a O(1) implementation.
        """
        return self.size

    def insert(self, curr, key, value):
        """
        Insert data into the TreeMap. This method must be recursive.
        When the key to insert already exists in the TreeMap, replace the existing TreeNode's value with 'value'.
        """
        if curr.key == key:
            curr.value = value
        elif curr.key > key:
            if curr.left:
                self.insert(curr.left, key, value)
            else:
                curr.left = TreeNode(key, value)
                self.size += 1
        else:
            if curr.right:
                self.insert(curr.right, key, value)
            else:
                curr.right = TreeNode(key, value)
                self.size += 1

    def __setitem__(self, key, value):
        """
        Support a call of the form tree[850123456]='Mike'. Make a call to the insert() method to do the actual
        insert. Also, handle the special case where the TreeMap is empty.
        """
        if not self.root:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            self.insert(self.root, key, value)

    def find(self, curr, key):
        """
        Find the key in the TreeMap and return its associated value. This method must be recursive.
        Raise a KeyError if the key is not in the TreeMap.
        """
        if not curr:
            raise KeyError
        elif curr.key == key:
            return curr
        elif key < curr.key:
            return self.find(curr.left, key)
        else:
            return self.find(curr.right, key)

    def __getitem__(self, key):
        """
        Support a call of the form 'x = tree[850123456]'. Make a call to the find() method to do the work.
        Raise a KeyError if the tree is empty.
        """
        # return self.find(self.root, key).value
        found, curr, parent = self._locate_node(key)
        if found:
            return curr.value
        else:
            raise KeyError

    def __contains__(self, item):
        """
        Support a call of the form 'x in tree'. Return True if x is a key in the tree, False otherwise.
        """
        found, curr, parent = self._locate_node(item)
        return found

    def height(self):
        """
        Return the height of the tree. Raise a ValueError if the TreeMap is empty.
        You may find it useful to implement a helper method that is recursive.
        """
        if self.root is None:
            raise ValueError

        return self.height_of_current_node(self.root)

    def height_of_current_node(self, node):
        # This helper method can be more concise, but I opt for clarity.
        # There are also many ways to implement this helper. This is just one example.
        left_subtree_height = -1
        right_subtree_height = -1

        if node.left is not None:
            left_subtree_height = self.height_of_current_node(node.left)
        if node.right is not None:
            right_subtree_height = self.height_of_current_node(node.right)

        if left_subtree_height > right_subtree_height:
            return 1 + left_subtree_height
        else:
            return 1 + right_subtree_height

    def _locate_node(self, key):
        """
        Find a node in the TreeMap based on the key. The method DOES NOT need to be recursive.
        Return three values:
        - found: True if the key was found in the TreeMap, False otherwise.
        - curr: the TreeNode containing the key
        - parent: the parent of the TreeNode containing the key
        :param key:
        :return:
        """
        found = False
        curr = self.root
        parent = None
        while curr is not None and not found:
            if key == curr.key:
                found = True
            elif key > curr.key:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left
        return found, curr, parent

    def _find_inorder_successor(self, node):
        """
        Return the in-order successor of a node, i.e., the node's leftmost right descendent, and that successors's parent.
        This method should ONLY be called on a node with both a left and a right child.
        Return the entire TreeNode objects.
        """
        curr = node.right
        parent = node
        while curr.left is not None:
            parent = curr
            curr = curr.left
        return curr, parent

    def __delitem__(self, key):
        """
        Support a call of the form 'del tree[850123456]'. Remove the node containing the key per the procedure
        discussed in class for deleting nodes from a BST.
        - Raise a KeyError if the key is not in the TreeMap.
        - You will need to use the _locate_node() and _find_inorder_successor() supporting methods.
        """
        self.found, self.cur, self.parent = self._locate_node(key)
        if not self.found or self.size == 0:
            raise KeyError
        if self.size == 1:
            self.cur = None
            self.parent = None
            self.root = None
            self.size-=1
            return
        self.parent2 = None
        if self.cur.left and self.cur.right:
            self.cur2, self.parent2 = self._find_inorder_successor(self.cur)
            if self.parent2.left.key == self.cur2.key:
                self.parent2.left = None
            else:
                self.parent2.right = None
                    
            if self.cur.left:
                self.cur2.left = self.cur.left
            if self.cur.right:
                self.cur2.right = self.cur.right
            
            if (self.root.key == self.cur.key):
                self.root = self.cur2
                self.cur2 = None
                self.parent2 = None     
            elif self.parent.key == self.root.key:
                if self.cur.key == self.root.left.key:
                    self.root.left = self.cur2
                else:
                    self.root.right = self.cur2
                self.parent = self.cur2
            else:
                self.parent = self.cur2
                
        else:
            if self.parent.left.key == self.cur.key:
                self.parent.left = None
            else:
                self.parent.right = None
            if self.cur.left:
                self.parent.right = self.cur.left
            else:
                self.parent.right = self.cur.right
        self.size-=1


    def traverse_inorder(self, node=None):
        """
        Perform an in-order traversal of the TreeMap to print each TreeNode. Note that __str__ is already defined
        for TreeNodes.
        - Do not print anything if the TreeMap is empty.
        """
        if not node:
            node = self.root
        if not node:
            return
        if node.left:
            self.traverse_inorder(node.left)
        print(node)
        if node.right:
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node=None):
        """
        Perform a preorder traversal of the TreeMap to print each TreeNode. Do not print anything if the TreeMap is empty.
        """
        if not node:
            node = self.root
        if not node:
            return
        print(node)
        if node.left:
            self.traverse_preorder(node.left)
        if node.right:
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node=None):
        """
        Perform a postorder traversal of the TreeMap to print each TreeNode. Do not print anything if the TreeMap is empty.
        """
        if not node:
            node = self.root
        if not node:
            return
        if node.left:
            self.traverse_postorder(node.left)
        if node.right:
            self.traverse_postorder(node.right)
        print(node)




if __name__ == '__main__':
    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    from treemap_tests import TestSuite
    import sys
    suite = TestSuite(sys.modules[__name__])
    suite.test_01_delitem()
    suite.test_02_inorder_traversal()
    suite.test_03_preorder_traversal()
    suite.test_04_postorder_traversal()
    if not suite.suite_passed:
        print('\u2717' * 5, "One or more tests in the test suite failed.")
    print(f">>> You have currently passed {suite.passed_count}/{suite.test_count} tests.")
