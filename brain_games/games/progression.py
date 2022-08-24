from random import randint


GAME_QUESTION = 'What number is missing in the progression?'


def generate_round():
    starting_number = randint(1, 50)
    progression_step = randint(1, 10)
    progression_lenght = randint(5, 10)
    progression = [starting_number, ]
    current_step = 1
    current_number = starting_number
    task = ''
    while current_step <= progression_lenght:
        current_number += progression_step
        progression.append(current_number)
        current_step += 1

    random_number = randint(0, (len(progression) - 1))
    result = str(progression[random_number])
    progression[random_number] = '..'
    for i in progression:
        task = task + str(i) + ' '
    return task, result
