class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self._is_empty():
            return None
        else:
            values = []
            node = self.last
            while node:
                values.append(node.value)
                node = node.prev
            return values

    def enqueue(self, value):
        if self._is_empty():
            node = QueueNode(value)
            self.first = node
            self.last = node
            self.length += 1
        else:
            node = QueueNode(value)
            node.next = self.first
            self.first.prev = node
            self.first = node
            self.length += 1

    def dequeue(self) -> QueueNode:
        if self._is_empty():
            return None
        else:
            node = self.last
            self.last = self.last.prev
            self.last.next = None
            self.length -= 1
            return node

    def _is_empty(self) -> bool:
        return self.length == 0


def test_queue_creation():
    q = Queue()
    assert q.first == None
    assert q.last == None
    assert q.length == 0
    assert q._is_empty() == True


def test_queue_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.first.value == 2
    assert q.last.value == 1
    assert q.length == 2


def test_queue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    node = q.dequeue()
    assert node.value == 1
    assert q.first.value == 3
    assert q.last.value == 2
    assert q.length == 2


def test_queue_empty_dequeue():
    q = Queue()
    node = q.dequeue()
    assert node == None


def test_queue_peek():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    values = q.peek()
    assert values == [1, 2, 3]


def test_queue_empty_peek():
    q = Queue()
    values = q.peek()
    assert values == None
