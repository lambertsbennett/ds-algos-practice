class DListNode:
    def __init__(self, value):
        self.value = value
        self.dref = None
        self.uref = None

    def previous(self):
        return self.uref

    def next(self):
        return self.dref

    def __str__(self) -> str:
        return f"value: {self.value}"


class DLinkedList:
    def __init__(self, value):
        node = DListNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value) -> None:
        node = DListNode(value)
        node.uref = self.tail
        self.tail.dref = node
        self.tail = node
        self.length += 1

    def prepend(self, value) -> None:
        node = DListNode(value)
        node.dref = self.head
        self.head.uref = node
        self.head = node
        self.length += 1

    def insert(self, index, value) -> None:
        if index == 0:
            self.prepend(value)
            self.length += 1
        elif index > self.length - 1:
            self.append(value)
            self.length += 1
        else:
            current_node = self.traverse(index - 1)
            new_node = DListNode(value)
            new_node.dref = current_node.dref
            new_node.uref = current_node
            current_node.dref = new_node
            self.length += 1

    def remove(self, index) -> None:
        if index == 0:
            self.head = self.head.dref
            self.head.uref = None
            self.length -= 1
        elif index > self.length - 1:
            print("trying to remove non-existent element.")
        elif index == self.length - 1:
            upstream_node = self.traverse(index - 1)
            upstream_node.dref = None
            self.tail = upstream_node
            self.length -= 1
        else:
            upstream_node = self.traverse(index - 1)
            downstream_node = upstream_node.dref.dref
            upstream_node.dref = downstream_node
            downstream_node.uref = upstream_node
            self.length -= 1

    def traverse(self, stop_index, v=False) -> DListNode:
        i = 0
        current_node = self.head
        while (current_node != None) and (i != stop_index):
            if v:
                print(f"{i}, value: {current_node.value}")
            current_node = current_node.next()
            i += 1
        return current_node


def test_dlinked_list_append():
    dll = DLinkedList(5)
    dll.append(6)
    assert dll.head.value == 5
    assert dll.tail.value == 6


def test_dlinked_list_prepend():
    dll = DLinkedList(5)
    dll.prepend(6)
    assert dll.head.value == 6
    assert dll.tail.value == 5


def test_dlinked_list_traverse():
    dll = DLinkedList(5)
    dll.prepend(6)
    node = dll.traverse(1)
    assert node.value == 5
    node = dll.traverse(0)
    assert node.value == 6


def test_dlinked_list_insert():
    dll = DLinkedList(5)
    dll.prepend(6)
    dll.insert(1, 4)
    assert dll.traverse(1).value == 4


def test_dlinked_list_remove():
    dll = DLinkedList(5)
    dll.prepend(6)
    dll.remove(0)
    assert dll.head.value == 5
    assert dll.tail.value == 5

def test_dlinked_list_remove_middle():
    dll = DLinkedList(5)
    dll.prepend(6)
    dll.prepend(7)
    dll.remove(1)
    assert dll.traverse(1).value == 5
    assert dll.tail.value == 5

def test_dlinked_list_remove_tail():
    dll = DLinkedList(5)
    dll.prepend(6)
    dll.prepend(7)
    dll.remove(2)
    assert dll.traverse(1).value == 6
    assert dll.tail.value == 6