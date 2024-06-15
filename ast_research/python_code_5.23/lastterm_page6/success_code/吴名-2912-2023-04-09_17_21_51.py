n=eval(input())
sum1=0
while 0==0:
  sum1+=n%10
  if n>=10:
    n=(n-n%10)/10
  elif n <10:
    sum1=int(sum1)
    break
print(sum1)

