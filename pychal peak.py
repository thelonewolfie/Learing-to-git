import requests


site=requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
file=open("banner.p","wb")

file.write(site.content)

file.close()
