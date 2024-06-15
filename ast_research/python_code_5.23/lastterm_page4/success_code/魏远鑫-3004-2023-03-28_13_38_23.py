list=eval(input())
if 1 in list:
    list.remove(1)
if 0 in list:    
    list.remove(0)
for x in list:
    for i in range(2,x//2+1):
        if x % i==0:
            list.remove(x)
print(list)
