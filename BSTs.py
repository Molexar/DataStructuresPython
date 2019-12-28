class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insertion(self.root, new_val, None)

    def search(self, find_val):
        return self.searcher(self.root, find_val)

    def searcher(self, node, find_val):
        if node:
            if node.value == find_val:
                return True
            else:
                if find_val > node.value:
                    return self.searcher(node.right, find_val)
                else:
                    return self.searcher(node.left, find_val)
        else:
            return False

    def insertion(self, node, new_val, parent):
        if node:
            if node.value > new_val:
                self.insertion(node.left, new_val, node)
            else:
                self.insertion(node.right, new_val, node)
        else:
            new_node = Node(new_val)
            if parent.value > new_val:
                parent.left = new_node
            else:
                parent.right = new_node


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
