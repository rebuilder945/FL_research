n=eval(input())
sum1=0
while n!=0:
  sum1+=n%10
  a=n%10
  n=n//10
  sum1+=a

print(sum1)

