lst=eval(input())

count=0
for i in lst:
    if i==0: count+=1

lst.sort()
ans=lst[count:]+[0]*count
print(ans)
