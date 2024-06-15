x=list(input())
for n in range(len(x)):
    x[n]=(int(x[n])+5)%10
if len(x)%2==0:
   for n in range(len(x)/2) :
      x[n]=x[-(n+1)]
else:
   for n in range((len(x)-1)/2):
      x[n]=x[-(n+1)]
for n in range(len(x)):
  print(x[n],end='')

