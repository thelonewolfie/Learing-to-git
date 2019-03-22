import datetime


for i in range(1,2000):
    if str(i).endswith('6'):
        if datetime.date(i,1,26).weekday()==0:
            print(i)
            
            
#mozart 1756


