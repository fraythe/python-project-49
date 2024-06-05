import prompt
from random import randint


def nod():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print(f'Question: {num1} {num2}')
        a = prompt.integer('Your answer: ')
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1
        r = num1 + num2
        if a != r:
            srry = print(f"'{a}' is wrong answer ;(. Correct answer was '{r}'.")
            srry2 = print(f"Let's try again, {name}!")
            return srry, srry2
            break
        else:
            print('Correct!')
            index = index + 1
    congrats = print(f'Congratulations, {name}!')
    return congrats
