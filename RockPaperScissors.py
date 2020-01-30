import random
import time

types = {"Scissors": "Paper", "Paper": "Rock", "Rock": "Scissors"}
AI = random.choice(list(types.keys()))

user = input("\nChoose 'Rock', 'Paper', or 'Scissors': ")
print("\nYou chose:", user)
time.sleep(0.7)
print("The AI chose:", AI)

time.sleep(0.4)
# If user ties:
if AI == user:
    print("\nTie!")
# If user loses:
elif types.get(AI) == user:
    print("\nYou lose!")
# If user wins:
else:
    print("\nYou won!")
time.sleep(1.5)
# =========================================================+
# The inspiration: someone in Xisumavoid's livestream chat |
# Main coding: Calamity34                                  |
# Dictionary: watch?v=Uj1ykZWtPYI#0601 at Python Discord   |
# =========================================================+
