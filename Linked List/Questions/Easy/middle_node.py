# Find Middle Node of Linked List

# Difficulty: Easy
# -------------------------------------------------------------------------------------------------------------------------

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: [1, 2, 3, 4, 5]
# Output: Node 3 from this list(Serialization: [3, 4, 5])


def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
