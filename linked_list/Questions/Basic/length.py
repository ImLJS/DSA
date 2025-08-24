# Length of Linked List

# Difficulty: Easy
# -----------------------------------------------------------------------------------------------------------
# Problem: Given a singly linked list, find length of linked list.

# Iterative Solution
def ll_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


# Recursive Solution
def ll_length_recur(head):
    if head is None:
        return 0
    return 1 + ll_length_recur(head.next)
