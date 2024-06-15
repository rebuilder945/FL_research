lst=eval(input())
for i in lst:
    if lst.count(i)>1:
        while i in lst:
            lst.remove(i)
            if lst.count(i)==1:
                break       
print(lst)

