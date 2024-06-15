n=eval(input())
sum1=0
while len(str(n))>0:
  sum1+=n%10
  n = int(str(n)[:-1])
print(sum1)

