n=0
lit=[]
while True:
    a=input()
    n+=1
    if a=='#':
        break
    b=int(a)
    lit.append(b)
print(n-1,end=' ')
print(sum(lit))

