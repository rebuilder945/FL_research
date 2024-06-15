b=[]
s=0
while s!='#':
    a=input()
    if a!='#':
        b.append(a)
    s=a
    if s=='#':
        break
print(len(b),sum(map(int,b)))
