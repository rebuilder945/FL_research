n=input()
b=[]
for i in range(len(n)):
    b.append(int(n[i]))
for j in range(len(b)):
    b[j]=(b[j]+5)%10
b.reverse()
for k in range(len(b)):
    print(b[k],end='')
