a = eval(input())
b = range(1,a+1)
c = list(b)
for i in range(0,len(c)-1,1):
    c[i]=c[i+1]
c[-1]=1
print(c)

