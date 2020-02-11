import random;l = list("0123456789ABCDEF");print("Your color: 0x" + "".join(random.choices(l, k=6)))
print("HEX string random:","".join(random.choices(l, k=64)))
