from random import randint


def progr():
    stop = randint(50, 60)
    step = randint(1, 9)
    numbers = list(range(randint(0, 15), stop, step))[:10]
    random_index = randint(0, len(numbers) - 1)
    r = numbers[random_index]
    numbers[random_index] = '..'
    string = ' '.join(map(str, numbers))
    question = f'{string}'
    return question, r
