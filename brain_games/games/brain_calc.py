from tokenize import Name
import prompt
import math
from random import randint, choice
from operator import add, sub, mul
from game_engine import engine 

#print("brain-calc\n\n\nWelcome to the Brain Games!")
#name = prompt.string('May I have your name? ')
#print(f"Hello, {name}!")



def calculator():
    game_name = "Brain-calc"
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operators = ("+", "-", "*")
    operator = choice(operators)
    expression = f"{num_1} {operator} {num_2}"

    print(f"{game_name}\n\n\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    score = 0
    win_score = 3
    while score < win_score:
        print(f'Question: {expression}')
        if operator == "+":
            result = add(num_1, num_2)
        elif operator == "-":
            result = sub(num_1, num_2)
        elif operator == "*":
            result = mul(num_1, num_2)
        answer_is = prompt.string('Your answer: ')
        if answer_is == str(result):
            print("Correct")
            score += 1
        else:
            print(f"'{answer_is}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            return
    
    print(f"Congratulations, Ivan!")
    return
        

calculator()
