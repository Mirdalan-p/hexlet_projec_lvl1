from random import randint


def game_logic():
        random_num = randint(1, 100)
        question = 'Answer "yes" if the number is even, otherwise answer "no".'
        task = random_num
        if random_num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        return  task, result