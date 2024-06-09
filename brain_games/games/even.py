from random import randint


def is_even():
    number = randint(1, 100)
    if number % 2 == 0:
        r = 'yes'
    else:
        r = 'no'
    question = f'{number}'
    return question, r
