# Reverse a linked list

# Difficulty: Easy
# -----------------------------------------------------------------------------------------------------------
# Problem: Given a linked list, reverse it.

# Iterative Solution
def reverse(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev


# Recursive Solution
def reverse_recur(head):
    if head is None or head.next is None:
        return head

    rest = reverse_recur(head.next)
    head.next.next = head
    head.next = None

    return rest
