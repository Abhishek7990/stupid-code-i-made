def baba():
    print("\nbaba is you \n is \nwin")

print("how to win:")
win = input("Type 'baba' to win: ")
if win == "baba":
    baba()
    print("     ")
    print("Congratulation")
else:
    print("Baba is not you!  Press 'Run' to restart.")