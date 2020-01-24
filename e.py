import random

answer = ["Yes", "No", "Perhaps"]


def eightball():
    input("What will be your question? ")
    print(random.choice(answer))


eightball()
