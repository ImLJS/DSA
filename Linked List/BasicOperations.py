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

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end="\n")
            temp = temp.next

    def append_at_end(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.size += 1
            return
        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = node

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        previous = None

        while current:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def append_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def append_at_position(self, data, position):
        if position < 0 or position > self.size:
            raise Exception("Invalid position")
        if position == 0:
            self.append_at_beginning(data)
            return
        if position == self.size:
            self.append_at_end(data)
            return
        node = Node(data)
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        node.next = temp.next
        temp.next = node
        self.size += 1


ll = LinkedList()
for i in range(10, 101, 10):
    ll.append_at_end(i)
print(ll.traversal())
