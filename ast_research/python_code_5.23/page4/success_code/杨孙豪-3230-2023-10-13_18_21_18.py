lst=eval(input())
lst.sort()
n=len(lst)
sum=0
for i in lst:
    sum+=i*10**lst.index(i)
print(sum)
