
# Infix to Postfix Conversion

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for ch in expression:

        if ch.isalnum():
            output.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if not stack:
                raise ValueError("Invalid expression")

            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   (precedence(stack[-1]) > precedence(ch) or
                    (precedence(stack[-1]) == precedence(ch)
                     and ch != '^'))):
                output.append(stack.pop())

            stack.append(ch)

    while stack:
        if stack[-1] == '(':
            raise ValueError("Invalid expression")
        output.append(stack.pop())

    return ''.join(output)


expression = input("Enter infix expression: ")

try:
    result = infix_to_postfix(expression)
    print("Postfix expression:", result)
except ValueError as e:
    print(e)
