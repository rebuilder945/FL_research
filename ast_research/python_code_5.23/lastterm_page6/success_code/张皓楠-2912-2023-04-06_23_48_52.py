n=eval(input())
sum1=0
while len(str(n))>0:
  sum1+=n%10
  n = int(n/10)
print(sum1)

