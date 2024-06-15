n=eval(input())
sum1=0
while sum1 <= 27 :
  sum1+=n%10
  n = n-n%10
print(sum1)

