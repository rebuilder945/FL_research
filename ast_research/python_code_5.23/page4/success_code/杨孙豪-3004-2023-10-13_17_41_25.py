lst=eval(input())
result=[]
for i in lst:
    for m in range(2,i):
        if i%m!=0:
            continue
        else:
            lst.remove(i)
print(lst)
