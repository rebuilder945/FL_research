a=input()
b=[]
for i in a:
    i=str((int(i)+5)%10)
    b.append(i)
b.reverse()
c=''
for i in b:
    c+=i
print(int(c))

