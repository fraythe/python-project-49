import prompt
from random import randint


def is_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        a = prompt.string('Your answer: ')
        if number % 2 == 0:
            r = 'yes'
        else:
            r = 'no'
        if a.lower() != r:
            srry = print(f"'{a}' is wrong answer ;(. Correct answer was '{r}'.")
            srry2 = print(f"Let's try again, {name}!")
            return srry, srry2
            break
        else:
            print('Correct!')
            index = index + 1
    congrats = print(f'Congratulations, {name}!')
    return congrats
