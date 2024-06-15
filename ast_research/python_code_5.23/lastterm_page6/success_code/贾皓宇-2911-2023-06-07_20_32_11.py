a=input()
b=[]
for x in range(len(a)):
    b.append(int(a[x]))
for i in range(len(b)):
    b[i]=(b[i]+5)%10
b.reverse()
print(''.join(str(x) for x in b))
