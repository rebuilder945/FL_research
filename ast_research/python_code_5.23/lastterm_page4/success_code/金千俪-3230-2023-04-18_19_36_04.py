lst=eval(input())
lst.sort(reverse=True)
if sum(lst)==0:
    print("0")
else:
    print(*lst,sep="")

