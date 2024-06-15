li_name=eval(input())
li_grade=eval(input())
nums=[]
for x in list(range(len(li_name))):
    nums.append(tuple((str(li_name[x]),int(li_grade[x]))))
print(nums)
