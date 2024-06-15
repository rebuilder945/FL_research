nums=[]
while True:
    x=input().split(" ")
    if x != ["ok"]:
        pass
        nums.append(x)
    else:
        break
di=dict(nums)
print(list(di.keys()))
print(list(di.items()))
if 'India' in list(di.keys()):
    print("yes")
else:
    print("no")
print(sum(list(di.items())))
