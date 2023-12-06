# A basic implementation of a linked list
class ListNode:
    def __init__(self, value):
        self.value = value
        self.ref = None

    def next(self):
        return self.ref

    def __str__(self) -> str:
        return f"value: {self.value}, ref: {self.ref}"


class LinkedList:
    def __init__(self, value):
        node = ListNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value) -> None:
        node = ListNode(value)
        self.tail.ref = node
        self.tail = node
        self.length += 1

    def prepend(self, value) -> None:
        node = ListNode(value)
        node.ref = self.head
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
            new_node = ListNode(value)
            new_node.ref = current_node.ref
            current_node.ref = new_node
            self.length += 1

    def remove(self, index) -> None:
        if index == 0:
            self.head = self.head.ref
            self.length -= 1
        elif index > self.length - 1:
            print("trying to remove non-existent element.")
        elif index == self.length - 1:
            upstream_node = self.traverse(index - 1)
            upstream_node.ref = None
            self.tail = upstream_node
            self.length -= 1
        else:
            upstream_node = self.traverse(index - 1)
            downstream_node = self.traverse(index + 1)
            upstream_node.ref = downstream_node
            self.length -= 1

    def traverse(self, stop_index, v=False) -> ListNode:
        i = 0
        current_node = self.head
        while (current_node != None) and (i != stop_index):
            if v:
                print(f"{i}, value: {current_node.value}, ref: {current_node.ref}")
            current_node = current_node.next()
            i += 1
        return current_node


ll = LinkedList(5)
ll.append(6)
ll.prepend(4)
ll.insert(1, 4.5)
ll.remove(1)
ll.traverse(stop_index=None, v=True)
