from random import randint, choice


def calc():
    operators = ['+', '-', '*']
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice(operators)
    if operator == '+':
        r = num1 + num2
    elif operator == '-':
        r = num1 - num2
    elif operator == '*':
        r = num1 * num2
    question = f'{num1} {operator} {num2}'
    return question, r
