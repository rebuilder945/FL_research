names=input().split(",")
nums=eval(input())
a=list(names)
ls=()
s=[]
for r in range(len(a)):
    ls=(a[r],nums[r])
    s.append(list(ls))
    c=[s]
print(c)
