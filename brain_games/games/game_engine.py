import prompt


def greeting():
    print(f"{game_name}\n\n\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(task)
    return name

def ans_comparison():
    if answer_is == result:
        print("Correct")
    else:
        print(f"'{answer_is}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
    
def wrong_answer():
    print(f"'{answer_is}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
    return
    
    