n=eval(input())
sum1=0
while sum1<n:
  sum1+=n%10
  n=int(n/10)
print(sum1)

