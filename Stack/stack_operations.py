# Stack

# Stack Operations
# 1. Push
# 2. Pop
# 3. Peek
# 4. Size
# 5. isEmpty

# Stack Implementation using Array


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not bool(self.stack)


S = Stack()

S.push("A")
S.push("B")
S.push("C")
print(S.is_empty())
print(S.peek())
print(S.pop())
print(S.pop())
print(S.peek())
print(S.pop())
print(S.is_empty())
