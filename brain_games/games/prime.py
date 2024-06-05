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
        a = prompt.string('Your answer: ')
        if num <= 1:
            r = 'no'
        else:
            r = 'yes'
            number_sqrt = int(math.sqrt(num))
            divisors = range(2, (number_sqrt + 1))
            for element in divisors:
                if num % element == 0:
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
