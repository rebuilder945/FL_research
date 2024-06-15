a=eval(input())
i=0
b=[]
while True:
    m=a[i]
    b.append(m)
    if m in b :
        a.remove(m)
        if m not in a:
            a.insert(i,m)
            i+=1
        
    else:
        i+=1
    if i>len(a)-1:
        break 
print(a)   
        
