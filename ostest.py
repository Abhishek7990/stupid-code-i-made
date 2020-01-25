import os

print(os.getcwd())

joe = "joe.txt"
file = open(joe,'r')
text = file.read()
print(text)
file.close()
file = open(joe,'w')
file.write(text + "g word")
file.close()
file = open(joe,'r')
text = file.read()
print(text)
