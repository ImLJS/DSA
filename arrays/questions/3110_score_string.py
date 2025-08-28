# Score of a String - Leetcode 3110 - Easy

# https://leetcode.com/problems/score-of-a-string/

# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters. Return the score of s.

# Example 1:
# Input: s = "abc"
# Output: 2
# Explanation: The score of the string is calculated as follows:
# The absolute difference between the ASCII values of 'a' and 'b' is |97 - 98| = 1.
# The absolute difference between the ASCII values of 'b' and 'c' is |98 - 99| = 1.
# The total score of the string is 1 + 1 = 2.

# Approach:
# 1. Initialize a variable to keep track of the score.
# 2. Iterate through the string from the first character to the second last character.
# 3. For each character, calculate the absolute difference between its ASCII value and the ASCII value of the next character.
# 4. Add this difference to the score.

def score_of_string(s: str) -> int:
    score = 0
    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
    return score

# Example usage:
s = "abc"
print(score_of_string(s))  # Output: 2
# Example 2:
s = "hello"
print(score_of_string(s))  # Output: 8