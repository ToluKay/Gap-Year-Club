name=input("What is your name? ")
score=int(input("What was your score? "))
if score>= 75:
    print("Congratulations " + name + "! You got an A1!")
elif score>= 70:
    print(name + " You got a B2.")
elif score>= 65:
    print(name + " You got a B3.")
elif score>= 60:
    print(name + " You got a C4.")
elif score>= 55:
    print(name + " You got a C5.")
elif score>= 50:
    print(name + " You got a C6.")
elif score>= 45:
    print(name + " You got a D7.")
elif score>= 40:
    print(name + " You got an E8.")
elif score<= 39:
    print(name + " You got an F9.")
