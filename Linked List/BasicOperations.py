# Linked List

# Traversing the list
# Inserting a data item in the list:
# Inserting a new data item (node) at the beginning
# Inserting a new data item (node) at the end of the list
# Inserting a new data item (node) in the middle/or at any given position in the list
# Deleting an item from the list:
# Deleting the first node
# Deleting the last node
# Deleting a node in the middle/or at any given position in the list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_begin(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

        return

    def insert_at_end(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def insert_at_location(self, data, index):
        node = Node(data)
        current = self.head
        pos = 0

        if self.head:
            while current and pos + 1 != index:
                pos += 1
                current = current.next

            if current:
                node.next = current.next
                current.next = node
            else:
                return -1

    def update(self, data, index):
        pos = 0
        current = self.head

        while current and pos != index:
            pos += 1
            current = current.next

        if current:
            current.data = data
        else:
            return -1

    def delete_begin(self):
        if self.head:
            self.head = self.head.next
        else:
            return

    def delete_end(self):
        if self.head:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        else:
            return

    def delete_index(self, index):
        current = self.head
        pos = 0

        while current and pos != index - 1:
            pos += 1
            current = current.next

        if current:
            current.next = current.next.next
        else:
            return

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_begin(4)

ll.delete_index(2)

ll.print()
