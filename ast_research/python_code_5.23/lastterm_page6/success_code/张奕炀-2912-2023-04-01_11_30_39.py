n=eval(input())
sum1=0
while True:
  sum1+=n%10
  n = n // 10
  if n == 0:
       break
print(sum1)

