import prompt
from brain_games.games import brain_calc, gcd, even, prime, progression


ROUNDS_COUNT = 3


def run(game):
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(f"{game.GAME_QUESTION}")
    
    for round in range(ROUNDS_COUNT):
        (task, result) = game.generate_round()
        print(f"Question: {task}")
        answer_is = prompt.string('Your answer: ')
        if answer_is == result:
            print("Сorrect!")
        else:
            print(f"'{answer_is}' is wrong answer ;(. "\
                f"Correct answer was '{result}'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    return
