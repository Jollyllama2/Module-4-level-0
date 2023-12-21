"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    score_number_one = simpledialog.askstring(title='wsp',prompt='What was your first test score(pls use tthe letter grades abc, letters in all caps)?')
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    score_number_two = simpledialog.askstring(title='wsp again',prompt='What was your second test score, hmm?')
    # TODO) Take the average score of both tests (total score / 2)
    if score_number_one == 'A' and score_number_two == 'A':
        messagebox.showinfo(title='wsp AGAIN', message='Amazing job getting an A on your first 2 tests, I just hope your scores did not drop...')
    if score_number_one == 'B' and score_number_two == 'B':
        messagebox.showinfo(title='WSP AGAIN',message= ' Getting a B is not bad at all, and is a pretty good grade for your first 2 tests, but you should probably spend more time studying, but great job!')
    if score_number_one == 'C' and score_number_two == 'C':
        messagebox.showinfo(title='wssssssssppppppppppp',message='Well those were your first 2 tests  I guess ¯\_(ツ)_/¯ ')
    if score_number_one == 'A' and score_number_two == 'B' or  score_number_one == 'B' and score_number_two == 'A':
        messagebox.showinfo(title='GamerhyunKr', message= 'Nice job on getting the A and the b is not bad either!')
    if score_number_one == 'A' and score_number_two == 'C' or  score_number_one == 'A' and score_number_two == 'A':
        messagebox.showinfo(title='hi',message=' huh, you got the best and worst score on your first 2 tests, huh...')
    if score_number_one == 'B' and score_number_two == 'C' or  score_number_one == 'C' and score_number_two == 'B':
        messagebox.showinfo(title='wsp again',message='Well, it is not that bad of a score for your first 2 tests, but it could be a bit better.')
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    pass
