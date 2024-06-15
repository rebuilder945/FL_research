n=eval(input())
sum1=0
while n>=1:
  sum1+=n%10
  n=int((n-n%10)*0.1)
print(sum1)

