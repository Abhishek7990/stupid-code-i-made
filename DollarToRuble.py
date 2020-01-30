import time

# Introduction:
print("Welcome to the stonk exchange!\n")
time.sleep(2)
way = input("Dollar to Ruble or backwards? (to R; to D): ")

# The money counting:
if way == "to R":
    try:
        amount = float(input("\nInput the amount of dollars: "))
        if amount < 0.01:
            raise ValueError
    except ValueError:
            print("\nNot a Number or is null!")
    else:
        answer = amount * 62
elif way == "to D":
    try:
        amount = input("\nInput the amount of rubles: ")
        if amount < 0.01:
            raise ValueError
    except ValueError:
        print("\nNot a Number or is null!")
    else:
        answer = amount / 62
else:
    print("\nIncorrect money type!")

# The result:
try:
    print("\nThe amount of money is: %f" % answer)
except NameError:
    print("\nTo restart the stonk exchange - run the code again.")
time.sleep(0.4)
print("\nThanks for using Stonk Exchange! Cya!")
time.sleep(0.5)
