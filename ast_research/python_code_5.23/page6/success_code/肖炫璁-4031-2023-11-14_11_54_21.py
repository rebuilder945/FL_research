n=eval(input())
sum1=0
while n>0:
  sum1+=n%10
  n=n-n%10
  sum1+=n%100
  n=n-n%100
  sum1+=n%1000
print(sum1)

