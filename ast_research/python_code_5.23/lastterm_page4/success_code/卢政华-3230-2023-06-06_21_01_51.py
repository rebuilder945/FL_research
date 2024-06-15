lst=eval(input())
lst.sort(reverse=True)
sum=''
for i in lst:
    sum+=str(lst[i])
print(int(sum))
