n=int(input())
j=1
b=-1
flag=False
while n>0:
  if n%10==5:
    print(j)
    if n<10:
      print(b)
    else:
      continue
  n=n//10
  j+=1
if j==1:
  print(b)

