# Balanced Parenthesis

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are
# balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.


def is_balanced_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] in ["(", "[", "{"]:
            stack.append(string[i])
        else:
            if (
                (string[i] == ")" and stack[-1] == "(")
                or (string[i] == "}" and stack[-1] == "{")
                or (string[i] == "]" and stack[-1] == "[")
            ):
                stack.pop()
            else:
                return False

    return not bool(len(stack))


arr = ["([][]({})", "([])", "((()))"]

for i in arr:
    print(is_balanced_parenthesis(i))
