from PIL import Image
img = Image.open('52.jpg')
print(img.size)
print(img.format)
img.show()