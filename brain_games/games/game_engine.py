import prompt
def engine(game_name):
    question = game_name.game_logic()
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count = 0
    win_count = 3   
    while count < win_count:
        (task, result) = game_name.game_logic()
        print(f"Question: {task}")
        answer_is = prompt.string('Your answer:')
    
        if answer_is == result:
            print("correct")
            count += 1
        else:
            print(f"'{answer_is}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}")
            return
    print(f"Congratulations, {name}!")
    return      
