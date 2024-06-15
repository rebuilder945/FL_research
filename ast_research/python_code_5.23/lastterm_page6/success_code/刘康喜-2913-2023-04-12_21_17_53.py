n=int(input())
j=1
b=-1
flag=False
while n>0:
  if n%10==5:
    print(j)
    b=2

  n=n//10
  j+=1
if b==2:
  print(b)

