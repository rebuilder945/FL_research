nums=eval(input(''))
a=[]
for i in nums:
    if nums.count(i)==1:
        a.append(i)
    else:
        pass
if len(a)==0:
    print('False')
else:
    a.sort(reverse=False)
    print(a)
