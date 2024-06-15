n=eval(input())
sum1=0
while type(sum1)==int:
  sum1+=n%10
  sum1+=n//10%10
print(sum1)

