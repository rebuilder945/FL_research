a=eval(input())
strnumbers=str(a)
for i in range(0,len(strnumbers)):
    b=int(strnumbers[i])
    d=(b+5)%10
    numbers=strnumbers.replace(str(b),str(d))
codenumbers=numbers[::-1]
print(int(codenumbers))

