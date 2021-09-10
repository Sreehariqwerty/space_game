# THIS CODE IS STILL IN DEVELOPMENT AND NOT TESTED
print('THIS CODE IS STILL IN DEVELOPMENT AND NOT TESTED !. THERE MIGHT BE BUG AND PLEASE FEEL FREE TO FIX IT ')
# Good 
import sys
from os import system ,name
from time import sleep
import time
import colorama as c 
from colorama import Fore, Back, Style
c.init(autoreset = True )
# Import the questions
import quest as q
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
az = q.az
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

1. If you are wrong once Game OVER!
2. There are 20 questions 
3. Lets start! 

''')
time.sleep(4)
print('Compiling the Quiz ...')
time.sleep(0.5)
print(Fore.GREEN + 'Reached target Quiz core(alpha) ...')
time.sleep(0.5)
print(Fore.YELLOW + 'Using Alpha v1.1(not recommmended) ...')
time.sleep(0.5)
print(Fore.GREEN + 'Reaced Target Quiz ')
time.sleep(0.9)
print('Initialising Game ....')
print(Fore.GREEN + 'Started Game!')
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
# Creating a clear screen method because python desnt have it :(

def clear():
    # For windows
    if name == 'nts':
        _ = system('cls')

    else:
        _ = system('clear')


clear()

time.sleep(0.5)
# game starts
# TODO make this random
print(a)
print('                                                                    ')
time.sleep(1)
print('''
Options:

(a) Because of no Gravity
(b) Because the skin doesnt shed in space because of radiation :)
(c) Beacause of staying inside a particular place for a long time.
(d) None of the above

Possible Options : a,b,c,d
''')
time.sleep(1)
questa = input('> ')

print('                                                                     ')


# check the answer
if questa == "a":
    print('Calculating you Answer (a)...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.GREEN + 'Nice! correct answer')
    print('                                                                     ')
elif questa == "b":
    print('Calculating your Answer(b) ...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.RED + 'Sorry :( wrong answer ')
    print('Exiting game ...')
    time.sleep(1)
    exit()

elif questa == "c":
    print('Calculating your Answer (c)...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.RED + 'Sorry :( wrong answer. You might want work on your science')
    print('Exiting game ...')
    time.sleep(1)
    exit()

elif questa == "d":
    print('Calculating your answer (d)...')
    print('                                                                     ')
    time.sleep(1)
    print(Fore.RED + ' :( Wrong asnwer !')
    time.sleep(0.5)
    print('Exiting game')
    time.sleep(1)
    exit()



else:
    print('Calculating your Answer ...')
    time.sleep(1)
    print('                                                                     ')
    print(Fore.RED + 'Sorry :( wrong input')
    print('Exiting game ...')
    time.sleep(1)
    exit()


clear()
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


elif ab == "a":
    print('Checking your answer ...(a)')
    print(Fore.RED + 'Sorry :( wrong answer ') 
    print('Exiting game ...')
    time.sleep(1)
    exit()

elif ab == "b":
    print('Checking your answer ...(b)')
    print(Fore.RED + 'Sorry Wrong answer')  
    print('Exiting game ...')
    time.sleep(1)
    exit()

elif ab == "c":
    print('Checking your answer ...(c)')
    print(Fore.RED + 'Wrong answer!')
    print('Exiting the Game ')
    exit()


else:
    print('Checking your answer ...(a)')
    print('Sorry Wrong input')
    print('Exiting game ...')
    time.sleep(1)
    exit()

clear()
print(c)
print('                                                                     ')
time.sleep(0.5)
print('''Options 

(a) Because the President was scared that they might bring new diseases
(b) To get media attention
(c) To get Fundings and Donations
(d) Because the President wa angry at them 

Possible Options : a,b,c,d
''')

time.sleep(0.5)
ac = input('> ')


# check the answer
if ac == "a":
    print('Checking your answer ...(a))')
    time.sleep(0.5)
    print(Fore.GREEN + 'Nice! correct answer')
    print('                                                                     ')

elif ac == "d":
    print('Checking your answer ...(d)')
    time.sleep(0.5)
    print(Fore.RED + 'Sorry :( wrong answer ')
    print('Exiting game ...')
    time.sleep(1)
    exit()

elif ac == "b":
    print('Checking your answer ...(b))')
    time.sleep(0.5)
    print(Fore.RED + 'Sorry Wrong answer')
    print('Exiting game ...')
    time.sleep(1)
    exit()

elif ac == "c":
    print('Checking your answer ...(c))')
    time.sleep(0.5)
    print(Fore.RED + 'Sorry :( wrong answer. Good try')
    print('Exiting game ...')
    time.sleep(1)
    exit()

else:
    print(Fore.RED + 'Invalid input')


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
time.sleep(0.5)
choic = input('> ')

# Check the answer
if choic == "a":
    print(Fore.RED + 'Wrong answer Sorry')
    print('Exiting the game ...')
    time.sleep(1)
    exit()

elif choic == "b":
    print(Fore.RED + 'Wrong answer Sorry')
    print('Exiting the game ...')
    time.sleep(1)
    exit()


elif choic == "c":
    print(Fore.RED + 'Wrong answer Sorry')
    print('Exiting the game ...')
    time.sleep(1)
    exit()


elif choic == "d":
    print(Fore.GREEN + 'You get to answer another time')
    print('                                                                     ')
    print('Nice ')
    time.sleep(1)

else:
    time.sleep(1)
    print(Fore.RED + 'Invalid Response please Try aganin')


# TODO add more questions and get a gui ny today and finish project by tommowor
