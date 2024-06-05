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
        users_answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if users_answer.lower() != right_answer:
            sorry = print(f"'{users_answer} is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
            return sorry
            break
        else:
            print('Correct!')
            index = index + 1
    congrats = print(f'Congratulations, {name}!')
    return congrats
