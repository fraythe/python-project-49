from random import randint
import math


def is_prime():
    num = randint(0, 100)
    question = f'{num}'
    if num <= 1:
        r = 'no'
    else:
        r = 'yes'
        number_sqrt = int(math.sqrt(num))
        divisors = range(2, (number_sqrt + 1))
        for element in divisors:
            if num % element == 0:
                r = 'no'
    return question, r
