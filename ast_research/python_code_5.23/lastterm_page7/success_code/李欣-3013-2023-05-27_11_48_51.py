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
for i in di:
    m.append(i)
m=sorted(m)
print(m)
print(n)
if 'India' in list(di.keys()):
    print("yes")
else:
    print("no")
print(sum(n))
