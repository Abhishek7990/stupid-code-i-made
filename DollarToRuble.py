import time

# Introduction:
print("Welcome to the stonk exchange!\n")
time.sleep(1)
way = input("Dollar to Ruble or backwards? (D-R; R-D): ")

# The money counting:
if way == "D-R":
    try:
        amount = float(input("\nInput the amount of dollars: "))
        if amount < 0.01:
            raise ValueError
    except ValueError:
            print("\nNot a Number or is null!")
    else:
        answer = amount * 62
elif way == "R-D":
    try:
        amount = float(input("\nInput the amount of rubles: "))
        if amount < 0.01:
            raise ValueError
    except ValueError:
        print("\nNot a Number or is null!")
    else:
        answer = amount / 62
else:
    print("\nError! Please, refer to the brackets.")

# The result:
try:
    print(f"\nThe amount of money is: {answer}")
except NameError:
    print("\nTo restart the stonk exchange - run the code again.")
time.sleep(0.6)
print("\nThanks for using Stonk Exchange! Cya!")
time.sleep(0.5)
