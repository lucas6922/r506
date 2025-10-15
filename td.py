from PIL import Image, ImageOps
import numpy as np
img:Image = Image.open("./lenna.png")

#EXERCICE 1

#img.show()

center = (img.width/2, img.height/2)
print(f'center: {img.getpixel(center)}')

data = list(img.getdata())

min = min(data)
max = max(data)

print(f'min : {min}')
print(f'max : {max}')



#EXERCICE 2

#img.rotate(90).show()

#EXERCICE 3

#ImageOps.invert(img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)).show()

#EXERCICE 4

print("---------------------\nEXERCICE 4")


img1:Image = Image.open("./camera1.png").convert("L")
img2:Image = Image.open("./camera2.png").convert("L")


arr1 = np.array(img1)
arr2 = np.array(img2)

mesure1 = arr1[0:80, 0:80]
mesure2 = arr2[0:80, 0:80]

average_pix_val_img1 = np.mean(mesure1)
average_pix_val_img2 = np.mean(mesure2)

standard_deviation_pix_val_img1 = np.std(mesure1)
standard_deviation_pix_val_img2 = np.std(mesure2)


#average_pix_val_img1 = np.mean(list(img1.getdata()))
#average_pix_val_img2 = np.mean(list(img2.getdata()))

#standard_deviation_pix_val_img1 = np.std(list(img1.getdata()))
#standard_deviation_pix_val_img2 = np.std(list(img2.getdata()))

print(f'moyenne img1 : {average_pix_val_img1}')
print(f'moyenne img2 : {average_pix_val_img2}')
print(f'ecart type img1 : {standard_deviation_pix_val_img1}')
print(f'ecart type img2 : {standard_deviation_pix_val_img2}')



#EXERCICE 5

print("---------------------\nEXERCICE 5")


nb = input("val transition : ")

try:
    nb = int(nb)
except:
    print("UN INT ON A DITTT")

#img1.point(lambda x: x + nb).show()

#EXERCICE 6


print("---------------------\nEXERCICE 6")

min = int(input("rentre unb nombre min pti con"))
max = int(input("rentre unb nombre max bolossssssss"))

def transform_pixel(x):
    if x < min:
        return min
    elif x > max:
        return max
    else:
        return x
    

img2222 = img1.point(transform_pixel)
img2222.show()


arr2 = np.zeros_like(arr1)
arr2[arr1 >= min] = arr1[arr1 >= min]
arr2[arr1 <= max] = max

arr3 = (arr2 - min) * 255 / (max - min)
arr3 = np.clip(arr3, 0, 255)

imgFJ3KJZ = Image.fromarray(arr2)
imgJHSKSOSAP = Image.fromarray(np.uint8(arr3))

imgJHSKSOSAP.show()
