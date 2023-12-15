# Get Nth Node From the End in a Linked List

# Difficulty: Easy
# ----------------------------------------------------------------------------------------------------

# Given a Linked List and a number N, write a function that returns the value at the Nth node
# from the end of the Linked List.

# Example 1:
# Input:
# LinkedList: 1->2->3->4->5
# N: 2
# Output: 4

# Example 2:
# Input:
# LinkedList: 10->20->30->40->50->60
# N: 6
# Output: -1

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

def nth_node_from_end(head, n):
    slow = head
    fast = head

    for i in range(n):
        if fast is None:
            return -1
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data
