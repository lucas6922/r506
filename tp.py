from PIL import Image
import numpy as np
import os

img = Image.open("./lenna.png")

#https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
nb_bit = img.mode

pixels = np.array(img)

pixels = (pixels // 16)

print(nb_bit)

image = Image.fromarray(pixels)

image.save("toto.png")
print(image.mode)


print(os.path.getsize("./lenna.png"))
print(os.path.getsize("./toto.png"))
print(os.path.getsize("./lenna.png") / os.path.getsize("./toto.png"))



#EXERCICE 2

git config --global user.email "lebon233@unicaen;fr"
git config --global user.name "lucas"

