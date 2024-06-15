n=eval(input())
sum1=0
while True:
  sum1+=n%10
  n=(n-n%10)/10
print(sum1)

