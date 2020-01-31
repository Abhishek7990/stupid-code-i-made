lang = input("'Russian' or 'English'? ")

# we need 2 helper mappings, from letters to ints and the inverse
if lang == "Russian":
    L2I = dict(zip("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ",range(33)))
    I2L = dict(zip(range(33),"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ"))

    plaintext = input("Message to encrypt: ")
elif lang == "English":
    L2I = dict(zip("ABCDEFGHIJKLMNOMPQRSTUVWXYZ",range(26)))
    I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    plaintext = input("Message to encrypt: ")
else:
    print("Not an option.")

key = 3

# encipher
try:
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
        else: ciphertext += c

    print(f"Your message: {ciphertext}")
except NameError:
    this = "is a blank line"

# ok this is not actually mine, all made by:
# https://gist.github.com/jameslyons/8701593
