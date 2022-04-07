# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    num0, operator, num2 = expression.split(' ')
    num0, num2 = float(num0), float(num2)
    if operator == '+':
        return num0 + num2
    elif operator == '-':
        return num0 - num2
    elif operator == '*':
        return num0 * num2
    elif operator == '/':
        return num0 / num2
    else:
        print('unknown operator!')
        return None
