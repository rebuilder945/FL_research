n=eval(input())
sum1=0
while n!=0:
  sum1+=n%10
  n=int((n-n%10)/10)
print(sum1)

