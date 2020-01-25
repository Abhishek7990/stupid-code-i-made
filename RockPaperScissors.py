import random

types = ["Rock", "Paper", "Scissors"]
AI = random.choice(types)

user = input("\nChoose 'Rock', 'Paper', or 'Scissors': ")
print("\nYou chose:", user)
print("The AI chose:", AI)

# If user ties:
if AI == "Rock" and user == "Rock" or AI == "Paper" and user == "Paper" or AI == "Scissors" and user == "Scissors":
    print("\nTie!")
# If user wins:
elif AI == "Rock" and user == "Paper" or AI == "Paper" and user == "Scissors" or AI == "Scissors" and user == "Rock":
    print("\nYou won!")
# If user loses:
elif AI == "Rock" and user == "Scissors" or AI == "Paper" and user == "Rock" or AI == "Scissors" and user == "Paper":
    print("\nYou lose!")
