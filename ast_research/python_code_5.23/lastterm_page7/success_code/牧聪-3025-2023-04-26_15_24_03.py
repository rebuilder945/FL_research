strs={}
sss=input().split()
for str in sss:
    if str in strs:
        strs[str]=strs[str]+1
    else:
        strs[str]=1
nums=list(strs.values())
t=max(nums)
for k,v in strs.items():
    if int(v)==t:
        print(k,v)
