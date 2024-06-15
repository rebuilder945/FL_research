m=0
n=0
d=[]
while m!='#':
    m=input()
    n+=1
    if m!='#':
       d.append(int(m))
print(n-1,sum(d))
