x=list(input())
for n in range(len(x)):
    x[n]=(int(x[n])+5)%10
for n in range(len(x)) :
    x[n]=x[-(n+1)]
m=eval(str(x))
print(int(m))

