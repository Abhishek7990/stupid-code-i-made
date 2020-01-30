import time

# Introduction:
print("Welcome to the stonk exchange!\n")
time.sleep(2)
way = input("Dollar to Ruble or backwards? (to R; to D): ")

# The money counting:
if way == "to R":
    amount = input("\nInput the amount of dollars: ")
    if float(amount) >= 1:
        answer = float(amount) * 62
    else:
        print("Incorrect!")
    
elif way == "to D":
    amount = input("\nInput the amount of rubles: ")
    if float(amount) >= 1:
        answer = float(amount) / 62
    else:
        print("Incorrect")
else:
    print("\nIncorrect money type!")

# The result:
print("\nThe amount of money is: %f" % answer)
time.sleep(0.4)
print("\nThanks for using Stonk Exchange! Cya!")
time.sleep(0.5)
