# Min Stack - LeetCode 155 - Medium

# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]

# Approach

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or val <= min_val:
            min_val = val
        self.stack.append((val,min_val))

    def pop(self) -> None:
        return self.stack.pop() if self.stack else None

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

# Explanation
# 1. Initialize an empty list stack to store tuples of (value, current_min).
# 2. In the push method, determine the current minimum by comparing the new value with the existing minimum (if any) and append a tuple of (value, current_min) to the stack.
# 3. The pop method removes and returns the top element of the stack if it's not empty.
# 4. The top method returns the value of the top element without removing it.
# 5. The getMin method returns the current minimum value from the top element of the stack.
# 6. All operations are performed in constant time O(1).

# Example usage
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Returns -3  
minStack.pop()
print(minStack.top())      # Returns 0
print(minStack.getMin())   # Returns -2
minStack.push(-1)
print(minStack.top())      # Returns -1
print(minStack.getMin())   # Returns -2
minStack.pop()
print(minStack.top())      # Returns 0