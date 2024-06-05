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
        right_answer = numbers[random_index]
        numbers[random_index] = '..'
        string = ' '.join(map(str, numbers))
        print(f'Question: {string}')
        users_answer = prompt.integer('Your answer: ')
        if users_answer != right_answer:
            sorry = print(f"'{users_answer} is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
            return sorry
            break
        else:
            print('Correct!')
            index = index + 1
    congrats = print(f'Congratulations, {name}!')
    return congrats
