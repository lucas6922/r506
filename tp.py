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

pixels_2 = np.array(img)
arr = pixels_2[::2, :]

image_ex2 = Image.fromarray(arr)
image_ex2.save("image_ex2.png")
print(os.path.getsize("./lenna.png"))
print(os.path.getsize("./image_ex2.png"))
print(os.path.getsize("./lenna.png") / os.path.getsize("./image_ex2.png"))


#EXERCICE 3

pixels_3 = np.array(img)
arr1 = pixels_3[:, ::2]
image_ex3 = Image.fromarray(arr1)
image_ex3.save("image_ex3.png")
print(os.path.getsize("./lenna.png"))
print(os.path.getsize("./image_ex3.png"))
print(os.path.getsize("./lenna.png") / os.path.getsize("./image_ex3.png"))


#EXERCICE 4

pixels_4 = np.array(img)
arr1 = pixels_4[::2, ::2]
image_ex4 = Image.fromarray(arr1)
image_ex4.save("image_ex4.png")
print(os.path.getsize("./lenna.png"))
print(os.path.getsize("./image_ex4.png"))
print(os.path.getsize("./lenna.png") / os.path.getsize("./image_ex4.png"))
