lst=eval(input())
ls=[]
for i in lst:
    if i!=0:
        ls.append(i)
for x in range(len(lst)-len(ls)):
    ls.append(0)
print(ls)



