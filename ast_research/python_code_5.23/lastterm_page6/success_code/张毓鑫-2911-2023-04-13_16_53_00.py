a=input()
b=[]
for i in a:
    i=str((int(i)+5)%10)
    b.append(i)
c=sum(b)
print(int(c))

