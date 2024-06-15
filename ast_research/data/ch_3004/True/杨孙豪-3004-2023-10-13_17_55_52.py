lst=eval(input())
if 0 in lst:
    lst.remove(0)
if 1 in lst:
    lst.remove(1)
result=[]
for i in lst[:]:
    for m in range(2,i):
        if i%m!=0:
            continue
        elif i in lst:
            lst.remove(i)
print(lst)
