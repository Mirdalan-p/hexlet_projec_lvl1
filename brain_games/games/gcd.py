from random import randint
import math

question = "Find the greatest common divisor of given numbers."


def game_logic():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    task = f"{num_1}, {num_2}"
    result = math.gcd(num_1, num_2)
    return task, str(result)
