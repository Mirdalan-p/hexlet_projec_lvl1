import prompt

ROUNDS_COUNT = 3


def run(game):
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(f"{game_name.question}")
    
    for round in range(ROUNDS_COUNT):
        (task, result) = game.game_logic()
        print(f"Question: {task}")
        answer_is = prompt.string('Your answer: ')
        if answer_is == result:
            print("Сorrect!")
            count += 1
        else:
            print(f"'{answer_is}' is wrong answer ;(. \
                Correct answer was '{result}'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    return
