lst=eval(input())
if sum(lst)==0:
    print("0")
else:
    lst1=lst.sort(reverse=True)
    print(*lst,sep="")

