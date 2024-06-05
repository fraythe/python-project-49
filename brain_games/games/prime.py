import prompt
from random import randint
import math

def is_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 0
    while index < 3:
        num = randint(0, 100)
        print(f'Question: {num}')
        users_answer = prompt.string('Your answer: ')
        if num <= 1:
            right_answer = 'no'
        else:
            right_answer = 'yes'
            number_sqrt = int(math.sqrt(num))
            divisors = range(2, (number_sqrt + 1))
            for element in divisors:
                if num % element == 0:
                    right_answer = 'no'
        if users_answer.lower() == right_answer:
            print('Correct!')
            index = index + 1
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
    congrats = print(f'Congratulations, {name}!')
    return congrats

