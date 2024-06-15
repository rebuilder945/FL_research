n=eval(input())
sum1=0
while n != 0:
  sum1+=n%10
  for i in range(1,len(n)):
          sum1 += (n//(10*i))%10
print(sum1)

