lst=eval(input())
lst.sort(reverse=True)
a=""
if lst[0]==0:
    print(0)
else:  
    for i in lst:
        a=a+str(i)
    print(a)
