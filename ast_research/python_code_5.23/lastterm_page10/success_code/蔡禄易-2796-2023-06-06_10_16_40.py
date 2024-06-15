a = input()
b = [x for x in a]
ls = ' '
c = [ ]
for i in b:
    if i.isdigit():
        c.append(i)
    else:
        c.append(ls)
if len(c) == 0:
    print("No digits")
else:
    ls1="".join(c)
    a = ls1.split(None)
    nums = [ ]
    for i in range(len(a)-1,0,-1):
        c = len(a[i])
        nums.append(c)
g = max(nums)
h = nums.index(g)
print(a[h-1]) 






    

