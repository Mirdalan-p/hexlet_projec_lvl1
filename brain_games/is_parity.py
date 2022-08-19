from calendar import c
import prompt
from random import randint

def parity_check():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_num = randint(1, 100)
    correct_answ_count = 0 
    answer_is = ' '
    while correct_answ_count < 3:
        print(f'Question: {random_num}')
        answer_is = prompt.string('Your answer: ')
        if answer_is == "Yes" and random_num == 0:
            print('Correct')
            correct_answ_count += 1
        elif answer_is == 'No' and random_num != 0:
            print('Correct')
            correct_answ_count += 1
        else:
            print('Your answer is wrong')
            correct_answ_count == 0
    print('Congratulations')
        
         