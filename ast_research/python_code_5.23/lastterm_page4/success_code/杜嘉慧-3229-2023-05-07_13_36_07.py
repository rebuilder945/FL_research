lst=eval(input())
lst.sort()
new=[]
flag=False
for i in lst:
    if lst.count(i)==1:
        new.append(i)
        flag=True
if flag:
    print(new)
else:
    print(flag)

