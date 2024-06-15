lst=eval(input())
m=lst.count(0)
if m==0:
    print(lst)
else:
    lst.pop(0)
for i in range(m):
    ls=lst+[0]
print(ls)

