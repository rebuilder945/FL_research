n=eval(input())
sum1=0
while i <= len(str(n)):
  sum1+=n%10
  n = n%10
  i += 1
print(sum1)

