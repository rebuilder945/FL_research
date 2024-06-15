a=eval(input())
i=0
b=[]
while True:
    m=a[i]
    b.append(m)
    if m in b :
        a.remove(m)
        
    else:
        i+=1
    if i>len(a):
        break 
print(a)   
        
