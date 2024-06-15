lst=eval(input())
nummin=min(lst)
nummax=max(lst)
while nummin in lst:
    lst.remove(nummin)
while nummax in lst:
    lst.remove(nummax)
print(lst)
        
