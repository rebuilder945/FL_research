x=list(input())
for n in range(len(x)):
    x[n]=(int(x[n])+5)%10
b=x.copy()
b.reverse()
for n in range(len(x)):
      x[n]=b[n]
for n in range(len(x)):
  print(x[n],end='')

