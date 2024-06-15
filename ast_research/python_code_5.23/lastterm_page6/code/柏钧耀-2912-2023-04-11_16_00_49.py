n=eval(input())
sum1=0
while True
  sum1+=n%10
  sum1=sum1-n%10
    a=list(str(n))
    c=[]
    for i in a:
      c.append(int(i))
    sum1=sum(c)
    break
print(sum1)

