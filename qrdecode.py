from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(r"qreee.jpg")
l = decode(img)
l=str(l[0][0])
#print(l)

for i in l.split(";"):
	j = i.split(":")
	print(j[len(j)-1])