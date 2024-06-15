b=[]
while True:
    a=input()
    if a=='#':
        break
    else:
        b.append(eval(a))
n=len(b)
m=sum(b)
print(n,m)

