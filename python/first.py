'''
Komentārs
pa vairākām rindiņām
©Andis 2019
'''
import math

x = 1  # INTEGER
y = 2
N = -4
pi = 3.14  # FLOATING POINT

sveiciens = "Welcome"  # STRING
ir_ziema = True  # BOOLEAN
grade = None
# print(x + y)


gads_raw = input('Please enter your birth year: ')

if gads_raw.isdigit():
    gads = int(gads_raw)
    dekade = math.floor((gads % 100) / 10)
    if dekade < 5:
        print('You have born before 1950')
    else:
        print('You have born after 1950')
else:
    print('Please enter a number!')


# print(dekade)

import sys
sys.exit()

a = input("Please enter first number: ")
b = input("Please enter second number: ")

c = int(a) + int(b)

print('Result:  ', c)
