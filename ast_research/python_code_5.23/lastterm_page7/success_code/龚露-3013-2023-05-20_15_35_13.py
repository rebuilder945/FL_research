nums=[]
while True:
    a = input().split()
    if a != ['ok']:
        nums.append(a)
    else:
        pass
        break
di = dict(nums)
keylist=[]
valuelist=[]
for k,v in di.items():
    keylist.append(k)
    valuelist.append(int(v))
keylist.sort()
valuelist.sort()
print(keylist)
print(valuelist)
if "India" not in keylist:
    print('no')
else:
    print('yes')
c=sum(valuelist)
print(c)

