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
n=[]
for i in list(di.values()):
    i=int(i)
    n.append(i)
print(n)
if 'India' in list(di.keys()):
    print("yes")
else:
    print("no")
print(sum(list(di.values())))
