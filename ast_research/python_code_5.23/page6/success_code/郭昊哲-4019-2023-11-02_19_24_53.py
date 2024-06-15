a=input()
b=[]
for i in range(len(a)):
    b.append(str((int(a[i])+5)%10))
b[0],b[-1]=b[-1],b[0]
b[1],b[-2]=b[-2],b[1]
print("".join(b))
