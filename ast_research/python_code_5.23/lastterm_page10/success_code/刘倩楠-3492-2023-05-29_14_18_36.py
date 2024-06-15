nums=eval(input())
ls=[]
for x in nums:
    m=nums.count(x)
    if x>1:
        ls.append(x)    
        print(ls[0])
    else:
        print("None")
