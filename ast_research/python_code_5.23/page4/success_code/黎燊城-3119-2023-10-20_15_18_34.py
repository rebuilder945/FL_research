nums=eval(input())
nums.reverse()
a=[]
for i in nums:
    if i not in a:
        a.append(i)
a.reverse()
print(a)
