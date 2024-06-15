n=eval(input())
b=[]
for i in range(len(n)):
    b.append(int(n[i]))
for i in range(len(b)):
    b[i]=(b[i]+5)%10
b.reverse()
for i in range(len(b)):
    print(b[i], end="")
