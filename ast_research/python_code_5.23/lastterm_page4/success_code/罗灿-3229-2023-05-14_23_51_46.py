nums=input()
lst=[]
for i in nums:
    if nums.count(i)==1:
        lst.append(i)
        lst.sort()
        print(lst)
    else:
        print(False)

