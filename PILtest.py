from PIL import Image
from PIL import ImageColor
import random
import PIL

ranhex = PIL.Image.New(RGB,(128, 128),color=random.randint(0, 0xFFFFFF))

ranhex = Image.save("C:\Users\Голоушкины\Documents\GitHub\stupid-code-i-made\PIL_Pics\randomhexpic.jpg")
