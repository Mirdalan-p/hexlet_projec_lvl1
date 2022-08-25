from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
        i = 0
        for devider in range(2, (num // 2 + 1)):
            if num % devider == 0:
                i += 1
        if num < 2:
            result = 'no'
        elif i == 0:
            result = 'yes'
        else:
            result = 'no'
        return result


def generate_round():
    random_num = randint(0, 100)
    task = f"{random_num}"
    result = is_prime(random_num)
    return task, result
