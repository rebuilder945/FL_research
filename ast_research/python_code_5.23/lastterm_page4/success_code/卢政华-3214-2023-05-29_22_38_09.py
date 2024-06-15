lst=eval(input())
for i in lst:
    if i ==0:
        del[i]
    s=lst.count(0)
lst.append(s*0)
print(lst)
