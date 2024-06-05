import prompt
from random import randint

def nod():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'Question: {a} {b}')
        users_answer = prompt.integer('Your answer: ')
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else :
                b = b % a
        res = a + b
        if users_answer == res:
            print('Correct!')
            index = index + 1
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{res}'.\nLet's try again, {name}!")
    congrats = print(f'Congratulations, {name}!')
    return congrats