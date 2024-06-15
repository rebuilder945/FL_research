a=eval(input())
nums=[]
for i in a:
    if a.count(i)==1:
        nums.append(i)
nums.sort()
print(*nums,sep=',')
