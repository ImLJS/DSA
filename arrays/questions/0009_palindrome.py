# Palindrome Number - LeetCode 9 - Easy

# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example 1:
# Input: 121
# Output: true
# Example 2:
# Input: -121
# Output: false

# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Approach 1: Convert the integer to a string and check if the string is equal to its reverse.
# Time Complexity: O(n)

def is_palindrome(x: int) -> bool:
    str_x = str(x)
    return str_x == str_x[::-1]

# Approach 2: Reverse half of the integer and compare it with the other half.
# Time Complexity: O(log10(n))
def is_palindrome_half_reversal(x: int) -> bool:
    # Negative numbers are not palindromes
    if x < 0:
        return False
    # Numbers ending in 0 are not palindromes unless the number is 0
    if x % 10 == 0 and x != 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        digit = x % 10
        reversed_half = reversed_half * 10 + digit
        x //= 10

    # For odd length numbers, we can get rid of the middle digit by reversed_half // 10
    return x == reversed_half or x == reversed_half // 10

# Example usage:
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False
print(is_palindrome_half_reversal(121))  # Output: True
print(is_palindrome_half_reversal(-121)) # Output: False