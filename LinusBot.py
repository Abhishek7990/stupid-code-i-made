import random

# RNG
RandomNumber = random.randint(4, 7)

# Instructions
print("Start number is:", RandomNumber)
print("Type anything else to not do a thing:")

# Add and Subtract functions
add = input("Type 'a' to add 1: ")
take = input("Type 'b' to subtract 1: ")

# The counting
if add == "a":
    addresult = int(RandomNumber) + 1

if take == "b":
    finalresult = int(addresult) - 1

# Result print
print("The result is:", finalresult)
