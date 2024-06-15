n=input()
i=0
l=[]
while i>=0:
    if n=='#':
        break
    else:      
        i+=1
        l.append(int(n))
        n=input()
print(i,sum(l))
