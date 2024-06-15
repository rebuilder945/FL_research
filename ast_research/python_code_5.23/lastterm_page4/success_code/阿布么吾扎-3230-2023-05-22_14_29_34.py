lst=eval(input())
lst.sort()
if lst[-1]==0:
    print(0)
else:
    lst=list(map(str,lst))
    lst.reverse()
    print("".join(lst))

