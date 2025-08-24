# To Get Nth Node in a Linked List

# Difficulty: Easy
# ----------------------------------------------------------------------------------------------------------

# Given a singly linked list and a position, return the node at that position in the linked list.
# The position of the head node is 0.

# Example 1:
# Input:
# LinkedList: 1->2->3->4->5
# Position: 2
# Output: 3

# Example 2:
# Input:
# LinkedList: 1->2->3->4->5
# Position: 4
# Output: 5


def nth_node(head, index):
    count = 0
    while head:
        if count == index:
            return head.data
        count += 1
        head = head.next
    return -1
