user_guess=int(input("Guess a number between 1 and 10 that I'm going to show "))
from random import randint
system_guess=randint(1,10)
if user_guess==system_guess:
    print("Congratulations, you got it!")
else:
    print("Sorry, try again.")
print(system_guess)
