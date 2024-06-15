n=int(input())
j=1
b=-1
flag=False
while n>0:
  if n%10==5:
    print(j)
    n=int((n-n%10)/10)
  n=n//10
  j+=1
if n==0 and j==1:
  print(b)

