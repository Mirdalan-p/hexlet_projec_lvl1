import prompt
import math
from random import randint, choice
from game_engine import greeting


def calculator():
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operators = ("+", "-", "*")
        operator = choice(operators)
        expression = f"{num_1} {operator} {num_2}"
        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        return str(expression), str(result)

print(calculator())