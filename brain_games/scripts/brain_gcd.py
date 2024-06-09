#!/usr/bin/env python3


from brain_games.games.gcd import nod
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    index = 0
    while index < 3:
        question, r = nod()
        print(f'Question: {question}')
        a = prompt.integer('Your answer: ')
        if a != r:
            srry = f"'{a}' is wrong answer ;(. Correct answer was '{r}'."
            srry2 = f"Let's try again, {name}!"
            print(srry)
            print(srry2)
            return
        else:
            print('Correct!')
            index = index + 1
    congrats = print(f'Congratulations, {name}!')
    return congrats


if __name__ == '__main__':
    main()
