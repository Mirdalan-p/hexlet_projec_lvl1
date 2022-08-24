from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_num = randint(0, 100)
    task = f"{random_num}"
    
    def prime_check():
        i = 0
        for devider in range(2, (random_num // 2 + 1)):
            if random_num % devider == 0:
                i += 1
        if i == 0:
            result = 'yes'
        else:
            result = 'no'
        return result
    result = prime_check()
    return task, result
