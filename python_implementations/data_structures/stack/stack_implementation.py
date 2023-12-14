# Simple stack based on a linked list.


class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self._is_empty():
            return None
        else:
            value_list = []
            node = self.top
            while node:
                print(node.value)
                value_list.append(node.value)
                node = node.next
            return value_list

    def push(self, value):
        if self._is_empty():
            new_node = StackNode(value)
            self.top = new_node
            self.bottom = new_node
            self.length += 1
        else:
            new_node = StackNode(value)
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    def pop(self) -> StackNode:
        if self._is_empty():
            return None
        else:
            node = self.top
            self.top = self.top.next
            self.length -= 1
            return node

    def _is_empty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False


def test_stack_creation():
    stack = Stack()
    assert stack.top == None
    assert stack.bottom == None
    assert stack.length == 0
    assert stack._is_empty() == True


def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.top.value == 1
    assert stack.bottom.value == 1
    assert stack.length == 1


def test_stack_multiple_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top.value == 2
    assert stack.bottom.value == 1
    assert stack.length == 2


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    node1 = stack.pop()
    node2 = stack.pop()
    empty = stack.pop()
    assert node1.value == 2
    assert node2.value == 1
    assert empty == None


def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    values = stack.peek()
    assert values == [2, 1]
