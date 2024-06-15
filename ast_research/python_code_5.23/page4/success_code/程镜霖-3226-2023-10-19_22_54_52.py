x=[]
for i in nums:
    x1=nums.count(i)
    if x1>len(nums)/2:
      x.append(i)
    else:
        pass
for i in x :
   if i in x:
      x.remove(i)
else:
      pass
if x==[]:
    print(False)
else:
    for i in x:
     print(i)





nums = eval(input())
y = search(nums)
print(y)


