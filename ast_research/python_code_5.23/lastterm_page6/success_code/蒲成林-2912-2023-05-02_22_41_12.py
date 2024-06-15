n=eval(input())
sum1=0
while n>0:
  sum1+=n%10
  sum1 = sum1 // 10
  break
print(sum1)

