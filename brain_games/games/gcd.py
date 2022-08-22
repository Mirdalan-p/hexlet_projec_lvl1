from random import randint
import math

def game_logic():
    question = "Find the greatest common divisor of given numbers."
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    task = f"{num_1}, {num_2}"
    result = math.gcd(num_1, num_2)
    return task, str(result)
