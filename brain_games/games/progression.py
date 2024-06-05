import prompt
from random import randint


def progr():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    index = 0
    while index < 3:
        stop = randint(50, 60)
        step = randint(1, 9)
        numbers = list(range(randint(0, 15), stop, step))[:10]
        random_index = randint(0, len(numbers) - 1)
        r = numbers[random_index]
        numbers[random_index] = '..'
        string = ' '.join(map(str, numbers))
        print(f'Question: {string}')
        a = prompt.integer('Your answer: ')
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
