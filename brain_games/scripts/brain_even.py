#!/usr/bin/env python3


from brain_games.games.even import is_even
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        question, r = is_even()
        print(f'Question: {question}')
        a = prompt.string('Your answer: ')
        if a.lower() != r:
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
