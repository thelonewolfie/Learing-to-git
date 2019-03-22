seq=[1,11]



for n in range(30):
    num=str(seq[-1])
    next=''
    count=1
    
    for i in range(len(num)-2):
        
        
        if num[i]==num[i+1]:
            count+=1
            
        else:
            next+=str(count)+num[i]
            
            count=1
            
    if num[-1]==num[-2]:
        count+=1
        next+=str(count)+num[-1]
    else:
        next+=str(count)+num[-2]+'1'+num[-1]
            
        
        count=1
        
        
    seq.append((next))
    
