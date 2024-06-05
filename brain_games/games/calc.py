import prompt
from random import randint, choice


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression')
    index = 0
    while index < 3:
        operators = ['+', '-', '*']
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = choice(operators)
        if operator == '+':
            right_answer = num1 + num2
        elif operator == '-':
            right_answer = num1 - num2
        elif operator == '*':
            right_answer = num1 * num2
        print(f'Question: {num1} {operator} {num2}')
        users_answer = prompt.integer('Your answer: ')
        if users_answer != right_answer:
            sorry = print(f"'{users_answer} is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
            return sorry
            break
        else:
            print('Correct!')
            index = index + 1
    congrats = print(f'Congratulations, {name}!')
    return congrats
