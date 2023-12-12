# Check if two linked lists are identical

# Difficulty: Easy
# -----------------------------------------------------------------------------------------------------
# Given two Singly Linked List, check if they are identical or not. Return true or false.

# Example 1:
# Input:
# LinkedList1: 1->2->3->4->NULL
# LinkedList2: 1->2->3->4->NULL
# Output: true

# Example 2:
# Input:
# LinkedList1: 1->2->3->4->NULL
# LinkedList2: 1->2->3->5->NULL
# Output: false


def identical(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False

        head1 = head1.next
        head2 = head2.next

    return True
