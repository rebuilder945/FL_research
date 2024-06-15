lst=eval(input())
new=[]
flag=False
for i in lst:
    if lst.count(i)==1:
        new.append(i)
        flag=True
if flag:
    new.sort()
    print(new)
else:
    print(flag)

