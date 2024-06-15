names=input().split(",")
nums=eval(input())
length=len(names)
final=[]
for i in range(length):
    new=[]
    new.append(names[i])
    new.append(nums[i])
    final.append(new)
print(final)
