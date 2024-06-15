n=int(input())
j=1
b=-1
flag=False
while n>0:
  if n%10==5:
    print(j)
    n=n-n%10
    if n=0:
      break
    else:
      continue

  n=n//10
  j+=1
if j==1:
  print(b)

