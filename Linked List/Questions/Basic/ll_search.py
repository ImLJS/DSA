# Linked Lst Search

# Difficulty: Easy
# -----------------------------------------------------------------------------------------------------------
# Problem: Given a linked list and a key in it, the task is to find the occurrence of given key in linked
# list. It may be assumed that the key is present in linked list.


def ll_search(head, key):
    if head is None:
        return False
    if head.data == key:
        return True
    return ll_search(head.next, key)
