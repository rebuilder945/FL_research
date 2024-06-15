nams=list(input().split(","))
nums=eval(input())
a=[]
for i in range(0,len(nams)):
    a.append([nams[i],nums[i]])
print(a)
