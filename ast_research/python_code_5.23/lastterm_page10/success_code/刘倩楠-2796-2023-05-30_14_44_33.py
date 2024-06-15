nums=input()
ls=[]
for x in list(range(len(nums))):
    for y in list(range(len(nums)+1)):
        ls.append(nums[x:y])
lt=[]
for i in list(range(len(ls))):
    for j in ls[i]:
        if j in "0123456789":
            lt.append(ls[i])
if len(lt)==0:
    print("No digits")
else:
    print(lt[-1])
