a=input()
i=0
nums=[]
while i>=0:
    if a=="#":
        break
    else:
        i=i+1
        nums.append(int(a))
        a=input()
print(i,sum(nums))
