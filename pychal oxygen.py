from PIL import Image
import requests

file=open("o.png","rb")

img=Image.open(file)

pix=[img.getpixel((i,img.height/2)) for i in range(img.width)]


pix=pix[1::7]

msg= "".join([chr(i) for i,j,k,l in pix if i==j==k]).split()

msg="".join(msg[9:])

msg=msg[1:-1].split(",")

for i in msg:
    print(chr(int(i)),end="")
    
