# Baseball Game - LeetCode 682 - Easy

# https://leetcode.com/problems/baseball-game/

# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
# 1. An integer x - Record a new score of x.
# 2. "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# 3. "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# 4. "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

# Return the sum of all the scores on the record after applying all the operations.

# Example 1:
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# Approach

def calPoints(ops):
    stack = []
    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)

# Explanation
# 1. Initialize an empty list stack to keep track of the scores.
# 2. Iterate through each operation in ops:
#    - If the operation is "C", remove the last score from the stack.
#    - If the operation is "D", double the last score and append it to the stack.
#    - If the operation is "+", sum the last two scores and append the result to
#      the stack.
#    - If the operation is an integer, convert it to an integer and append it to
#      the stack.
# 3. After processing all operations, return the sum of the scores in the stack.

# Example usage

ops1 = ["5", "2", "C", "D", "+"]
print(calPoints(ops1))  # Output: 30
ops2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(calPoints(ops2))  # Output: 27
ops3 = ["1"]
print(calPoints(ops3))  # Output: 1