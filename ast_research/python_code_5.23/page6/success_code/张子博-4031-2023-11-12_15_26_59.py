n=eval(input())
sum1=0
while n>0:
  sum1+=n%10
  n=(n-n%10)/10
  sum1=int(sum1)
print(sum1)

