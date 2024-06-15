lst=eval(input())
lst.sort(reverse=True)
m=""
if sum(lst)==0:
    print("0")
else:
    for i in lst:
        m+=str(i)
    print(m)    

