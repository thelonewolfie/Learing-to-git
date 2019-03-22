from PIL import Image



file=open("cave.jpg","rb")

img=Image.open(file)


new1=Image.new("RGBA",img.size,"black")
new2=Image.new("RGBA",img.size,"black")

for i in range(img.width):
    for j in range(img.height):
        if (i+j)%2==0:
            new1.putpixel((i,j),img.getpixel((i,j)))
        else:
            new2.putpixel((i,j),img.getpixel((i,j)))
            
        
new1.save("even.png")
new2.save("odd.png")

