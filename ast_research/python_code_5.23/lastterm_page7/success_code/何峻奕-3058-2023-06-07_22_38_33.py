nums=[]
end="q"
for x in iter(input,end):
    nums.append(x)
lst=[]
for i in nums:
    a=nums.count(i)
    lst.append(a)
for x in nums:
    if nums.count(x)==max(lst):
        print(x,max(lst))
        break
