lst=eval(input())
num=[]
if 1 in lst:
    lst.remove(1)
if 0 in lst:
    lst.remove(0)
for x in range (len(lst)):
    for i in range (2,lst[x]):
        if lst[x]% i==0:
            break
    else:
        num.append(lst[x])
            
print(num)
    
