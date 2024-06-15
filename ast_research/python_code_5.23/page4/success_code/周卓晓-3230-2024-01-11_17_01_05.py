lst=eval(input())
lst.sort(reverse=True)
s=""
if lst[0]!=0:
    for x in lst:
        s+=str(x)
    print(s)
else:
    print("0")


