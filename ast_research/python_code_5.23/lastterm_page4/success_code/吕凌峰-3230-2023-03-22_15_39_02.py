a=eval(input())
a.sort(reverse=True)
sum=0
for x in range(0,len(a)):
    sum=sum*10+a[x]
print(sum)
