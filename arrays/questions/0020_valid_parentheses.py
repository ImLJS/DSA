# Valid Parentheses - Leetcode 20 - Easy

# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Approach: Adding opening brackets to stack and checking for closing brackets

# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char not in mapping:
            stack.append(char)
        
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            
            stack.pop()
        
    return not stack  # If the stack is empty, all brackets were matched

# Explanation
# 1. Initialize an empty stack to keep track of opening brackets.
# 2. Create a mapping dictionary to match closing brackets with their corresponding opening brackets.
# 3. Iterate through each character in the string:
#    - If the character is an opening bracket, push it onto the stack.
#    - If it's a closing bracket, check if the stack is empty or if the top of the stack doesn't match the corresponding opening bracket. If either condition is true, return False.
#    - If it matches, pop the top of the stack.
# 4. After processing all characters, if the stack is empty, return True (all brackets were matched); otherwise, return False.

# Example usage
s1 = "()"
print(isValid(s1))  # Output: True
s2 = "()[]{}"
print(isValid(s2))  # Output: True
s3 = "(]"
print(isValid(s3))  # Output: False
s4 = "("
print(isValid(s4))  # Output: False