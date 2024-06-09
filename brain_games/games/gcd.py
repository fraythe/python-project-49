from random import randint

def nod():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    r = num1 + num2
    return question, r
