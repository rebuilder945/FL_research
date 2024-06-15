nums=eval(input())
nums.sort()
for x in nums:
    if nums.count(x)==1:
        print(x,end=",")
    else:
        print("Flase")
        
