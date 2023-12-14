class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BSTNode(value)
        if self.root == None:
            self.root = node
        else:
            search_node = self.root
            while search_node:
                if (value < search_node.value) and not (search_node.left):
                    search_node.left = node
                    break
                elif value < search_node.value:
                    search_node = search_node.left
                elif (value > search_node.value) and not (search_node.right):
                    search_node.right = node
                    break
                elif value > search_node.value:
                    search_node = search_node.right

    def lookup(self, value):
        search_node = self.root
        while search_node:
            if value > search_node.value:
                search_node = search_node.right
            elif value < search_node.value:
                search_node = search_node.left
            else:
                return search_node
        return None

    def _is_leaf(node: BSTNode) -> bool:
        return not (node.left and node.right)


def test_bst_init():
    bst = BinarySearchTree()
    assert bst.root == None


def test_bst_insert_empty():
    bst = BinarySearchTree()
    bst.insert(1)
    assert bst.root != None
    assert bst.root.value == 1


def test_bst_insert_lt_gt():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(0)
    assert bst.root.left.value == 0
    assert bst.root.right.value == 2


def test_bst_lookup():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(0)
    node = bst.lookup(2)
    assert node.value == 2
    node = bst.lookup(3)
    assert node == None
