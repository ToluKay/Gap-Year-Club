name=input("What is your name? ")
credit=int(input("How many credits have you taken? "))
if credit >= 84:
    print(name+ " You are a senior.")
elif credit >= 54:
    print(name+ " You are a junior.")
elif credit >= 24:
    print(name+ " You are a sophomore.")
elif credit <= 23:
    print(name+ " You are a freshman.")
