# Remove Duplicates from Sorted List

# Difficulty: Easy
# -----------------------------------------------------------------------------------------------------------

# Problem: Given a sorted linked list, delete all duplicates such that each element appear only once.

# Input: 1->1->2->3->3
# Output: 1->2->3

# Input: 1->1->2->3->3->4->4->5
# Output: 1->2->3->4->5

# Solution:
# Time Complexity: O(n)
# Space Complexity: O(1)


def remove_duplicates(head):
    if head is None:
        return head

    # We use two pointers: current and next
    # If current.data == next.data, we set current.next = next.next
    # Else, we move current to the next node
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head


# -----------------------------------------------------------------------------------------------------------
