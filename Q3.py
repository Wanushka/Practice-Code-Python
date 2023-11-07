#Question 03

import random

a=int(input("enter a number :")) 
b= random.randint(1, 9)
while a!= b:
   b= int(input('Guess a number between 1 to 9 :'))

print('Well guessed!')
