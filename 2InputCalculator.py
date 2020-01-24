a = input("Enter the first number: ")
action = input("Choose an action (add/subtract/divide/multiply/expotent): ")
b = input("Enter the second number: ")

if action == "add":
    equals = int(a) + int(b)
    print("Your output:", equals)
elif action == "subtract":
    equals = int(a) - int(b)
    print("Your output:", equals)
elif action == "divide":
    equals = int(a) / int(b)
    print("Your output:", equals)
elif action == "multiply":
    equals = int(a) * int(b)
    print("Your output:", equals)
elif action == "expotent":
    equals = int(a) ** int(b)
    print("Your output:", equals)
elif action is not "add" or "subtract" or "divide" or "multiply" or "expotent":
    print("Incorrect action!")
