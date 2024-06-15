a=input()
b=[]
for i in range(0,len(a)):
    b.append(str((int(a[i])+5)%10))
for i in range(0,len(b)//2):
    b[i],b[len(b)-1-i]=b[len(b)-1-i],b[i]
print("".join(b))
