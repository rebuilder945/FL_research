a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
b=[(x+5)%10 for x in b ]
c=b.copy()
b.reverse()
print("".join(str(x) for x in b ))


