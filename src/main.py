# THIS CODE IS STILL IN DEVELOPMENT AND NOT TESTED
# Good
from os import system ,name
from time import sleep
import time
import colorama as c
from colorama import Fore, Back, Style
c.init(autoreset = True )
# Import the questions
import quest as q

ar = Fore.LIGHTWHITE_EX + "==> "

# Acesses the variable for the questions
a = q.a
b = q.b
c = q.c
d = q.d
e = q.e
g = q.g
k = q.k
i = q.i
m = q.m
p = q.p
z = q.z
f = q.f
h = q.h
n = q.n
l = q.l
ab = q.ab
aa = q.aa
ac = q.ac
ad = q.ad
af = q.af
# Done importing question
# Some design
# TODO use some sys for --help also add different levels to the same.
print(Fore.LIGHTBLUE_EX + '''
    ----     -------       /\           ------------    -------------
  /         |      |      /  \          |               |
  |         |      |     /    \         |               |
   \ _      |______|    /      \        |               |----------
       \    |          /--------\       |               |
       |    |         /          \      |               |
   ___/     |        /            \     |               |
            |       /              \    -------------   -------------

            ''')
print(Fore.CYAN + '''These are the rules

1. If you are wrong once Quiz OVER!
2. There are 20 questions
3. Lets start!

''')
time.sleep(4)
print(ar + Fore.GREEN + 'Compiling the Quiz ...')
time.sleep(0.5)
print(ar + Fore.GREEN + 'Reached target Quiz core ...')
time.sleep(0.5)
print(ar + Fore.YELLOW + 'Using  v1.2 ...')
time.sleep(0.5)
print(ar + Fore.GREEN + 'Reaced Target Quiz ')
time.sleep(0.9)
print(ar + Fore.GREEN + 'Initialising Quiz ....')
print('                     ')
print(ar + Fore.GREEN + 'Started Quiz!')
time.sleep(2)
print('3')
time.sleep(0.5)
print(2)
time.sleep(0.5)
print(1)
print('           ')
print('Go!')
time.sleep(0.5)

print('                                                   ')

def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


clear()
time.sleep(0.5)
# game starts
# Print the first question
print(a)
print('                                                                    ')
time.sleep(1)
print('''
Options:

(a) Because of no Gravity
(b) Because the skin doesnt shed in space because of radiation :)
(c) Beacause of staying inside in a particular place for a long time.
(d) None of the above

Possible Options : a,b,c,d
''')
questa = input('> ')

print('                                                                     ')

answers = 0
# check the answer 1
if questa == "a":
    print('Calculating you Answer (a)...')
    time.sleep(0.5)
    print('                                                                     ')
    print(Fore.GREEN + 'Nice! correct answer')
    time.sleep(2)
    print('           ')
    answers = answers + 1
    print(Fore.GREEN + 'You have gained 1 point by answering this questions')
    print('           ')
    print(Fore.CYAN + "Your score is  " + str(answers))
    time.sleep(2)
    print('                                                                     ')

elif questa == "b":
    print('Calculating your Answer(b) ...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.RED + 'Sorry :( wrong answer ')
    print('           ')
    print(Fore.RED + 'You dont earn any points for this answer')
    print('           ')
    print(Fore.CYAN + "Your  score is  " + str(answers) )
    time.sleep(2)
    time.sleep(1)

elif questa == "c":
    print('Calculating your Answer (c)...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.RED + 'Sorry :( wrong answer. You might want work on your science')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.CYAN + "Your  score " + str(answers) + " Correct")
    print('                                                                     ')
    time.sleep(0.5)
    print(Fore.RED + 'You dont earn any points for this answer')
    time.sleep(2)

elif questa == "d":
    print('Calculating your answer (d)...')
    print('                                                                     ')
    time.sleep(1)
    print(Fore.RED + ' :( Wrong asnwer !')
    print('                                                                     ')
    time.sleep(1)
    print(Fore.GREEN + 'You dont earn any points for this answer')
    print('                                                                     ')
    print(Fore.CYAN + "Your score is  " + str(answers))
    time.sleep(2)



else:
    print('Calculating your Answer ...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.RED + 'Sorry :( wrong input')
    print('                                                                     ')
    time.sleep(1)
    print(Fore.CYAN + "Your score is" + str(answers))
    time.sleep(2)


clear()
time.sleep(0.5)
# Print second question
print(b)
time.sleep(0.5)
print('                                                                     ')
print('''Options

(a) 0.5 day
(b) 1 day
(c) 1 month
(d) 12 months

Possible Options : a,b,c,d
''')

# check 2nd answer
time.sleep(0.5)
ab = input('> ')

# check the answer
if ab == "d":
    print('Checking your answer ...(d)')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.GREEN + 'Nice! correct answer')
    print('                                                                     ')
    time.sleep(2)
    print("You have Earned one point  ")
    print('                                                                     ')
    print(Fore.CYAN + "You total score is:  " + str(answers))
    time.sleep(2)


elif ab == "a":
    print('Checking your answer ...(a)')
    print(Fore.RED + 'Sorry :( wrong answer ')
    print('                                                                     ')
    time.sleep(1)
    print("You dont get any points for this answer")
    print('                                                                     ')
    print(Fore.CYAN + "You total score is:  " + str(answers))
    time.sleep(2)

elif ab == "b":
    print('Checking your answer ...(b)')
    print(Fore.RED + 'Sorry Wrong answer')
    print('                                                                     ')
    time.sleep(1)
    print("You dont get any points for this answer")
    print('                                                                     ')
    print(Fore.CYAN + "You total score is:" + str(answers) + " Correct")
    time.sleep(2)

elif ab == "c":
    print('Checking your answer ...(c)')
    print(Fore.RED + 'Wrong answer!')
    print('                                                                     ')
    time.sleep(2)
    print(Fore.CYAN + "Your total score is: " + str(answers))
    print('                                                                     ')
    print("You dint get any points from this answer ")
    time.sleep(2)


else:
    print('Checking your answer ...(a)')
    print('                                                                     ')
    print('Sorry Wrong input this is counted as a wrong answer ^-^ ')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.CYAN + "You have got " + str(answers) + " Correct")
    time.sleep(2)

# Clear the screen
clear()
# Print the third qiestion
print(c)
print('                                                                     ')
time.sleep(0.5)
print('''Options

(a) Because the President was scared that they might bring new diseases
(b) To get media attention
(c) To get Fundings and Donations
(d) None of the above

Possible Options : a,b,c,d
''')

ac = input('> ')


# check the answer for 3rd question
if ac == "a":
    print('Checking your answer ...(a))')
    time.sleep(0.5)
    print(Fore.GREEN + 'Nice! correct answer')
    time.sleep(2)
    print('                                                                     ')
    print(Fore.CYAN + "You total score is: " + str(answers))
    time.sleep(0.5)
    print('                                                                     ')
    print('You have got 1 point from this answer')
    time.sleep(2)

elif ac == "d":
    print('Checking your answer ...(d)')
    print('                                                                     ')
    time.sleep(0.5)
    print(Fore.RED + 'Sorry :( wrong answer ')
    print('                                                                     ')
    print("You dont get any points for this answer")
    time.sleep(1)
    print('                                                                     ')
    print(Fore.CYAN + "You total score is: " + str(answers))
    time.sleep(2)

elif ac == "b":
    print('Checking your answer ...(b))')
    time.sleep(0.5)
    print(Fore.RED + 'Sorry Wrong answer')
    print('                                                                     ')
    time.sleep(1)
    print("You dont get any points for this answer")
    print('                                                                     ')
    time.sleep(1)
    print(Fore.CYAN + "Your total score is:  " + str(answers) )
    time.sleep(2)

elif ac == "c":
    print('Checking your answer ...(c))')
    time.sleep(0.5)
    print('                                                                     ')
    time.sleep(2)
    print(Fore.RED + 'Sorry :( wrong answer. Good try')
    print('                                                                     ')
    print("You dont get any points for this answer")
    print('                                                                     ')
    time.sleep(1)
    print(Fore.CYAN + "You have got " + str(answers) + " Correct")

else:
    print(Fore.RED + 'Invalid input')
    print('                                                                     ')
    print(Fore.CYAN + "You have got " + str(answers) + " Correct")
    time.sleep(2)


clear()
print(d)
print('                                                                     ')
print('''Options

Possible Options : a,b,c,d

(a) 1000 Earths
(b) 10,000 Earths
(c) 1,00,000 Earths
(d) 10,00,000 Earths

''')
choic = input('> ')

# Check the answer 4
if choic == "a":
    print(Fore.RED + 'Wrong answer Sorry')
    time.sleep(2)
    print('                                                                     ')
    time.sleep(1)
    print(Fore.CYAN + "You have got " + str(answers) + " Correct")
    print('                                                                     ')
    print("You have got no points for this answer")
    time.sleep(2)

elif choic == "b":
    print(Fore.RED + 'Wrong answer Sorry')
    print('                                                                     ')
    print("You dont get any points for this answer")
    print('                                                                     ')
    time.sleep(1)
    print(Fore.CYAN + "You have got " + str(answers) + " Correct")
    time.sleep(2)

elif choic == "c":
    print(Fore.RED + 'Wrong answer Sorry')
    print('                                                                     ')
    time.sleep(1)
    print("You dont get any points for this answer")
    print('                                                                     ')
    print(Fore.CYAN +  "You have got " + str(answers) + " Correct")
    time.sleep(2)


elif choic == "d":
    print(Fore.GREEN + 'Nice correct answer Quiz Over!')
    print('                                                                     ')
    time.sleep(2)
    print('Nice ')
    print('                                                                     ')
    time.sleep(1)
    print(Fore.CYAN + "You have got " + str(answers) + " Correct")
    time.sleep(2)

else:
    time.sleep(1)
    print(Fore.RED + 'Invalid Response please Try aganin')
    print('                                                                     ')
    print(Fore.CYAN + "You have got " + str(answers) + " Correct out of 4 questions")
    time.sleep(2)
    print('                                                                     ')


print('                                          Results                                                                     ')
print('  ')

if answers == 4:
    print(ar + Fore.GREEN + "Nice you are intelligent ^_^ ")

elif answers == 3:
    print(ar + Fore.LIGHTGREEN_EX + 'Good! But you have scope to improve')

elif answers == 2:
    print(ar + Fore.YELLOW + 'Good try you gave it your all')

else:
    print(ar + Fore.RED + 'Try again next time')

