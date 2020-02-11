import random
d = input("First number: ")
e = input("Second number: ")
try:
    n = range(int(d),int(e))
    a = random.choice(n)
    print(f"Your random number: {a}")
except ValueError:
    print("Number not found!")    
input("Press Enter to exit")
