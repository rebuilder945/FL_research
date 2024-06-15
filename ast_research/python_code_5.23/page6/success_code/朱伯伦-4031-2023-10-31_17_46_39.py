n=eval(input())
sum1=0
while type(n)==int:
  sum1+=n%10
  n=(n|10)
print(sum1)

