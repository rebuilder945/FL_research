n=int(input())
j=1
b=-1
flag=False
while n>0:
  if n%10==5:
    print(j)
    flag=1
  n=n//10
  j+=1
if flag=0:
  print(b)

