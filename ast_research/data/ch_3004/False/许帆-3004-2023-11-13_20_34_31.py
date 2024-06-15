a = eval(input())
lst=[]
if 2 in a:
    lst.append(2)
for i in a:
    for x in range(2,i-1):
        if i/x==0:
            break
        else:
            lst.append(i)
print(lst)
