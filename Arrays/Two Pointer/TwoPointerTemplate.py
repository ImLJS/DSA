# Two Pointer Template

# Q. Check if the array is a palindrome


def isPalindrome(arr):
    L, R = 0, len(arr) - 1

    while L <= R:
        if arr[L] != arr[R]:
            return False
        L += 1
        R -= 1
    return True


arr = [1, 2, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5]

print(isPalindrome(arr))  # True
print(isPalindrome(arr2))  # False
