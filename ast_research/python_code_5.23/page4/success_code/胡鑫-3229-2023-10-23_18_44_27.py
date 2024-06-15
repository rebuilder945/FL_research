list = eval(input())
xinlist = []
for x in list:
    if list.count(x) > 1:
        pass
    else:
        xinlist.append(x)
if len(xinlist) == 0:
    print("False")
elif len(xinlist) > 0:
    xinlist.sort()
    print(*xinlist,sep = ",")
