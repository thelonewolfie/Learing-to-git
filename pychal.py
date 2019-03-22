import pickle
import urllib.request


url=r"http://www.pythonchallenge.com/pc/def/banner.p"

a= urllib.request.urlopen(url)
content=a.read()

data=pickle.load(urllib.request.urlopen(url))    
    
    
for i in data:
    for j,k in i:
        print(j*k)