lst=eval(input())
for i in lst.copy():
    if lst.count(i)>1:
        lst.remove(i)
print(lst)        

