import sys
try:
    a = int(input("Enter the first number: "))
    x = input("Enter the equation type (+ | - | * | / | **): ")
    b = int(input("Enter the second number: "))
except ValueError:
    print("Number Not Detected!")
    sys.exit()

def looper():
    loop = input("Would you like to input another number? (Y/N) ")
    if loop == "Y":
        print('Okay!')
    elif loop == "N":
        print("Okay!")
        sys.exit()
    else:
        print("Answer not executed: counting as N...")
        sys.exit()

if x == "+":
    ans = a + b
    print(f"Answer: {ans}")
    looper()
elif x == "-":
    ans = a - b
    print(f"Answer: {ans}")
    looper()
elif x == "*":
    ans = a * b
    print(f"Answer: {ans}")
    looper()
elif x == "/":
    ans = a / b
    print(f"Answer: {ans}")
    looper()
elif x == "**":
    ans = a ** b
    print(f"Answer: {ans}")
    looper()
else:
    print("I did not get the equation right! Restarting...")
    sys.exit()

if looper() == "Y":
    while True:
        y = input("Enter an equation: ")
        c = int(input("Enter another number: "))

        if y == "+":
            ans = ans + c
            print(f"Answer: {ans}")
        elif y == "-":
            ans = ans - c
            print(f"Answer: {ans}")
        elif y == "*":
            ans = ans * c
            print(f"Answer: {ans}")
        elif y == "/":
            ans = ans / c
            (f"Answer: {ans}")
        elif y == "**":
            ans = ans ** c
            print(f"Answer: {ans}")
        else:
            print("I did not get the equation right! Restarting...")
            sys.exit()
        breaker = input("Would you like to end the program? (Y/N) ")
        if breaker == "Y":
            print("Okay!")
            break
        elif breaker == "N":
            print("Okay!")
        else:
            print("Not an Answer! Ending the program...")
            break
