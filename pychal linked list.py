
import requests
import re
import winsound

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num="8022"
state=1
reg=re.compile(r"nothing\sis\s(\d+)")


count=1
while state:
    
    count+=1
    site= requests.get(url+num)
    mo=reg.search(site.text)
    print(num,site.text)
    with open("nothing.txt",'a') as file:
        file.write(site.text+"\n")

    
                   
                
    for i in mo.groups():
        
        tempsite=requests.get(url+i)
        if tempsite.status_code==200:
            num=i
            break
        else:
            continue
        state=0
        
    if len(site.text)>29:
        winsound.Beep(2000,2000)
        exec(input())
        

   
       
        
        

         

