import random
from random import randint
from brain_games.scripts.brain_games import main as welcome_user

def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count<3:
        a = randint(1,100)
        b = randint(1, 100)
        cor_ans = get_ans(a, b, count)
        str = input("Your answer: ")
        answer = int(str)
        if answer == cor_ans:
            print("Correct!")
            count+=1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

def get_ans(a, b,op):
    if op == 0:
        print(f'Question: {a} {b}')
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return b
    elif op == 1:
        print(f'Question: {a} {b}')
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return b
    else: 
        print(f'Question: {a} {b}')
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return b
