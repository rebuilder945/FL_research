a=eval(input())
i=0
b=[]
while True:
    m=a[i]
    if m in b:
        a.remove(m)
        if not m in a():
            a.insert(i,m)
    else:
        i+=1
    if i>len(a):
        break 
print(a)   
        
