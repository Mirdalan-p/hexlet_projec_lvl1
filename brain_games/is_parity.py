from calendar import c
import prompt
from random import randint


print("brain-games\nWelcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f"Hello, {name}!")


def parity_check():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answ_count = 0 
    while correct_answ_count < 3:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        answer_is = prompt.string('Your answer: ')
        if answer_is == "yes" and random_num % 2 == 0:
            print('Correct')
            correct_answ_count += 1
        elif answer_is == 'no' and random_num % 2 != 0:
            print('Correct')
            correct_answ_count += 1
        else:
            if answer_is == 'yes' and random_num % 2 != 0:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            elif answer_is == 'no' and random_num %2 == 0:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            correct_answ_count = 0
    print(f"Congratulations, {name}!")

parity_check()
      
         