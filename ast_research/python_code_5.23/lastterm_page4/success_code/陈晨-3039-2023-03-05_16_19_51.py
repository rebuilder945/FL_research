lst=eval(input())
lst.sort()
num=len(lst)
nummin=lst[0]
nummax=lst[num-1]
while nummin in lst:
    lst.remove(nummin)
while nummax in lst:
    lst.remove(nummax)
print(lst)
        
