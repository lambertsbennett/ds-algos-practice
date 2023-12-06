from ll_implementation import LinkedList


class ReversibleLinkedList(LinkedList):
    def reverse(self):
        if self.length == 1:
            pass
        else:
            first = self.head
            self.tail = self.head
            second = first.next()
            while second:
                tmp = second.next()
                second.ref = first
                first = second
                second = tmp
            self.head.ref = None
            self.head = first


rll = ReversibleLinkedList(5)
rll.append(6)
rll.append(7)
rll.reverse()
rll.traverse(None, v=True)
