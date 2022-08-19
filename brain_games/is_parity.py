from calendar import c
import prompt
from random import randint


print("brain-games\nWelcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f"Hello, {name}!")
random_num = randint(1, 100)

def parity_check():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answ_count = 0 
    while correct_answ_count < 3:
        print(f'Question: {random_num}')
        answer_is = prompt.string('Your answer: ')
        if answer_is == "Yes" and random_num % 2 == 0:
            print('Correct')
            correct_answ_count += 1
        elif answer_is == 'No' and random_num % 2 != 0:
            print('Correct')
            correct_answ_count += 1
        else:
            if answer_is == 'Yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,' + name + '!'")
                parity_check()
    print(f"Congratulations, {name}!")


        
         