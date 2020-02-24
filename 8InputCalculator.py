import sys
try:
    a = int(input("Enter the first number: "))
    x = input("Enter the equation type (+ | - | * | / | **): ")
    b = int(input("Enter the second number: "))
except ValueError:
    print("Number Not Detected!")
    sys.exit()

if x in ["*","/","**","+","-"]:
    ans = None
    exec(f"ans = a {x} b")
    print(f"Answer: {ans}")
    loop = input("Would you like to input another number? (Y/N) ").upper()
    if loop == "Y":
        print('Okay!')
    elif loop == "N":
        print("Okay!")
        sys.exit()
    else:
        print("Answer not executed: counting as N...")
        sys.exit()
else:
    print("I did not get the equation right! Restarting...")
    sys.exit()

if loop == "Y":
    while True:
        y = input("Enter an equation: ")
        c = int(input("Enter another number: "))
        if y in ["*","/","**","+","-"]:
            exec(f"ans = ans {y} c")
            print(f"Answer: {ans}")
        else:
            print("I did not get the equation right! Restarting...")
            sys.exit()
        breaker = input("Another number? (Y/N) ").upper()
        if breaker == "Y":
            print("Okay!")
        elif breaker == "N":
            print("Okay!")
            break
        else:
            print("Not an Answer! Ending the program...")
            break
