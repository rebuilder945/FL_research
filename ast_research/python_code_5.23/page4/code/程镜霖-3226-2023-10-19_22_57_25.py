def search()
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
     x1=i
return x1






nums = eval(input())
y = search(nums)
print(y)


