nums=[]
while True:
    x=input().split(" ")
    if x != ["ok"]:
        pass
        nums.append(x)
    else:
        break
di=dict(nums)
n=[]
m=[]
for i in list(di.values()):
    i=int(i)
    n.append(i)
n=sorted(n)
for p in n:
    for key,value in di.items():
        if p==int(value):
            m.append(key)
print(m)
print(n)
if 'India' in list(di.keys()):
    print("yes")
else:
    print("no")
print(sum(n))
