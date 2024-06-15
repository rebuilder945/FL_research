x=list(input())
for n in range(len(x)):
    x[n]=(int(x[n])+5)%10
for n in range(len(x)) :
    x[n]=x[-(n+1)]
print(x[0:],end='')

