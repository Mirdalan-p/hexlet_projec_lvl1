import prompt


def engine():
    print(f"{game_name}\n\n\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count = 0
    win_count = 3

    while count < win_count:
        print(f"Question: {task}")
        answer_is = prompt.string('Your answer:')
    
        if str(answer_is) == result:
            print("correct")
            count += 1
        else:
            print("'{answer_is}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}")
            return
    print(f"Congratulations, {name}!")
    return      

    
    