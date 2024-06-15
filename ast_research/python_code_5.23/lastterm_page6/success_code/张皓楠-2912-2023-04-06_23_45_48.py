n=eval(input())
sum1=0
while len(n)>1:
  sum1+=n%10
  n = n[:-1]
print(sum1)

