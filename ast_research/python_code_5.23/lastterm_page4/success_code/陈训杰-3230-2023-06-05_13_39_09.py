lst=eval(input())
lst.sort(reverse=True)
if lst[0]==0:
    print(0)
else:
    lst=list(map(str,lst))
    print("".join(lst))
