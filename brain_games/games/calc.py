import prompt
from random import randint, choice


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    index = 0
    while index < 3:
        operators = ['+', '-', '*']
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = choice(operators)
        if operator == '+':
            res = num1 + num2
        elif operator == '-':
            res = num1 - num2
        elif operator == '*':
            res = num1 * num2
        print(f'Question: {num1} {operator} {num2}')
        users_answer = prompt.integer('Your answer: ')
        if res == users_answer:
            print('Correct!')
            index = index + 1
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{res}'.\nLet's try again, {name}!")
    congrats = print(f'Congratulations, {name}!')
    return congrats
