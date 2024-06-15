nums=[]
while True:
    dummy=input().split(" ")
    if dummy != ["ok"]:
        nums.append(dummy)
    else:
        pass
        break
di=dict(nums)
keylist=[]
valuelist=1
for k,v in di.items():
    keylist.append(k)
    valuelist.append(int(v))
keylist.sort()
valuelist.sort()
print(keylist)
print(valuelist)
if 'India' not in keylist:
    print("no")
else:
    pass
print("yes")
print(sum(valuelist))
