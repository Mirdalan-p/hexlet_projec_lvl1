from random import randint


def game_logic():
        game = 'brain-even'
        random_num = randint(1, 100)
        task = random_num
        if random_num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        return task, result, game