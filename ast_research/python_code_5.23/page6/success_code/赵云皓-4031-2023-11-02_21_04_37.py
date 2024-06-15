n=eval(input())
sum1=0
while n!=1:
  sum1+=n%10
  n=(n-sum1)/10;sum1=int(sum1)
print(sum1)

