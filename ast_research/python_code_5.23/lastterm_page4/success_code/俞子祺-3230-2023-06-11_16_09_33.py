ls=eval(input())
ls=list(ls)
if ls==000:
    print(000)
ls.sort()
ls.reverse()
print("".join(map(str,ls)))

