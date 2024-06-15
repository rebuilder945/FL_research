nums=[]
while True:
    a = input().split()
    if a != ['ok']:
        nums.append(a)
    else:
        pass
        break
di = dict(nums)
ls1=list(dict.keys())
ls2=list(dict.values())
print(ls1)
print(ls2)
if "India" not in ls1:
    print('no')
else:
    print('yes')
c=sum(ls2)
print(c)

