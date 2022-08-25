from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_num):
    if random_num < 2:
        return 'no'
    for i in range(2, random_num):
        if random_num % i == 0:
            return 'no'
    return 'yes'


def generate_round():
    random_num = randint(0, 100)
    task = f"{random_num}"
    result = is_prime(random_num)
    return task, result
