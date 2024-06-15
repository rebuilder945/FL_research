a=input()
b=[]
for x in range(len(a)):
    b.append(int(a[x]))
for y in range(len(b)):
    b[y]=(b[y]+5)%10
b.reverse()
for z in range(len(b)):
    print(b[z],end='')
