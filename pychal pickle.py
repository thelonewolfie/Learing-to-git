import os,re,zipfile

loc=r".\channel\\"
txt=".txt"
s="90052"
z=r"E:\Ajoy\python\a.zip"
msg=open("msg.txt","a")

reg=re.compile(r"(\d+)")


text=""

zip=zipfile.ZipFile(z)

for i in range(len(os.listdir(".\channel"))):
    
    temp=open(loc+s+txt,"r").read()
    
    s=reg.search(temp).group()
    text=zip.getinfo(s+txt).comment
    print(text.decode("utf-8"),end="")
    with open("msg.txt","a") as msg:
        msg.write(text.decode("utf-8"))
    
    
msg.close()
    
    
        
        

        
        


