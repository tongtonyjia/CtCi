class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = QueueNode(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def remove(self):
        head = self.head

        if self.head is not None:
            self.head = self.head.next

        return head

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head is None
