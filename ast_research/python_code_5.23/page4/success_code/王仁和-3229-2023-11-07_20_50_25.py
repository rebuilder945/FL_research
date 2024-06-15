nums = eval(input())
finlist = []
for x in nums:
    if nums.count(x) > 1:
        pass
    else:
        finlist.append(x)
if len(finlist) == 0:
    print("False")
elif len(finlist) > 0:
    finlist.sort()
    lista = ','.join(str(i) for i in finlist)
    print(lista)

