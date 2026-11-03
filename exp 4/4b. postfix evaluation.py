
# Postfix Expression Evaluation

def evaluate_postfix(expression):
    stack = []

    for ch in expression:

        if ch.isdigit():
            stack.append(int(ch))

        else:
            if len(stack) < 2:
                print("Invalid Expression")
                return

            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)

            elif ch == '-':
                stack.append(a - b)

            elif ch == '*':
                stack.append(a * b)

            elif ch == '/':
                stack.append(a // b)

            else:
                print("Invalid Operator")
                return

    if len(stack) == 1:
        print("Result:", stack.pop())
    else:
        print("Invalid Expression")


expression = input("Enter postfix expression: ")

evaluate_postfix(expression)
