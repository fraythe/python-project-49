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
        if number % 2 == 0 and users_answer.lower() == 'yes' or (number % 2 != 0 and users_answer.lower() == 'no'):
            print('Correct!')
            index = index + 1
        elif number % 2 == 0 and users_answer.lower() == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!") 
        elif number % 2 != 0 and users_answer.lower() == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        elif users_answer.lower != 'no' and users_answer.lower() != 'yes':
            print(f"'{users_answer}' is wrong answer ;(.\nLet's try again, {name}!")
    congrats = print(f'Congratulations, {name}!')
    return congrats
