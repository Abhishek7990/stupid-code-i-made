# lego city game
import time

def lose():
    print("\nYou did not do the thing and the man has drowned.")
    print("You failed!")
    time.sleep(0.8)

try:
    print("Director  of fire station: A MAN HAS FALLEN INTO THE RIVER IN LEGO CITY. WHAT SHOULD WE START?")
    time.sleep(0.5)
    start = input("\nType 'start the new rescue helicopter': ").lower()

    time.sleep(0.5)
    if start == "start the new rescue helicopter":
        print("\nHEY!")
        time.sleep(0.5)
        print("\nBuild the helicopter and off to the rescue!")
        time.sleep(0.5)
        build = input("Type 'build the copter' to build the helicopter: ").lower()

    time.sleep(0.5)
    if build == "build the copter":
        print("\nYou have successfully built a copter!")
        time.sleep(0.5)
        print("*nyooom*")
        time.sleep(0.5)
        print("Prepare the lifeline!")
        time.sleep(0.5)
        lifeline = input("Type 'prepare' to prepare the lifeline: ").lower()

    time.sleep(0.5)
    if lifeline == "prepare":
        print("\nLower the stretcher!")
        time.sleep(0.5)
        stretcher = input("Type 'lower' to lower the stretcher: ").lower()

    time.sleep(0.5)
    if stretcher == "lower":
        print("\nAnd make the rescue!")
        time.sleep(0.5)
        rescue = input("Type 'make the rescue' to make the rescue: ").lower()

    time.sleep(1)
    if rescue == "make the rescue":
        print("\nDirector: Congratulations, you have saved the man!")
        time.sleep(0.7)
        print("\nTHE NEW EMERGENCY COLLECTION FROM LEGO CITY")
        time.sleep(0.7)
except NameError:
    lose()
