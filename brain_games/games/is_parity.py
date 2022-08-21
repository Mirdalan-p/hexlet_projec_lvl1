import prompt
from random import randint


print("brain-even\n\n\nWelcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f"Hello, {name}!")


def parity_check():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    win_score = 3
    while score < win_score:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        answer_is = prompt.string('Your answer: ').lower()
        if answer_is == "yes" and random_num % 2 == 0:
            print('Correct')
            score += 1
        elif answer_is == 'no' and random_num % 2 != 0:
            print('Correct')
            score += 1
        else:
            if answer_is == 'yes' and random_num % 2 != 0:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            elif answer_is == 'no' and random_num % 2 == 0:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            elif answer_is != 'yes' or 'no':
                if random_num % 2 == 0:
                    print(f"'{answer_is}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
                elif random_num % 2 != 0:
                    print(f"'{answer_is}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    return
