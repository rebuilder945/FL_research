lst=eval(input())
lst.sort(reverse=True)
sum=''
for i in range(len(lst)):
    sum+=str(lst[i])
print(lst(sum))
