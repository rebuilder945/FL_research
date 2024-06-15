a=eval(input())
a.sort(reverse=True)
sum=0
for i in a:
    sum=sum*10+i
print(sum)
