n=eval(input())
sum1=0
while n//10!=0 :
  sum1+=n%10
  n=n//10
  if 0<=n<10:
          sum1+=n

print(sum1)

