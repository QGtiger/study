import pytesseract
from PIL import Image

image = Image.open(r'C:\Users\Administrator\Desktop\test\1.png')
image = image.convert('L')
threshold = 115
table=[]
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
code = pytesseract.image_to_string(image)
print(code)
image.show()