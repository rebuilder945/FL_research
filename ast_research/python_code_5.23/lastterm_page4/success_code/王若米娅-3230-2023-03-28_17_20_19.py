lst=eval(input())
lst.sort(reverse=True)
if max(lst)==0:
    print("0")
else:
    print(*lst,sep='')


