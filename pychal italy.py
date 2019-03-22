import PIL.Image as i

pic=i.open("wire")
pix=[pic.getpixel((i,0)) for i in range(10000)]

count=0
xmin=0
ymin=0
ymax=100
xmax=100
x,y=0,0

new=i.new("RGB",(100,100))

while count<10001:
    ymin,ymax=xmin,xmax 
    for y in range(ymin,ymax):
        new.putpixel((x,y),pix[count])
        print(x,y,count)
        count+=1
    
    xmin+=1
    for x in range(xmin,xmax):
        new.putpixel((x,y),pix[count])
        count+=1
        print(x,y,count)
    
    
    ymax-=1
    for y in reversed(range(ymin,ymax)):
        new.putpixel((x,y),pix[count])
        count+=1
        print(x,y,count)
        
    xmax-=1    
    for x in reversed(range(xmin,xmax)):
        new.putpixel((x,y),pix[count])
        count+=1
        print(x,y,count)
        
    if count==10000:
        break
        
    
        
    


        
        
    
    
    
        
        
        
        
        




