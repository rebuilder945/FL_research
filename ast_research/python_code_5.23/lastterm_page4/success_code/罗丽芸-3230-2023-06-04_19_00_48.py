ls=eval(input())
ls.sort()
if ls[-1]==0:
    print(0)
else:
    ls=list(map(str,ls))
    ls.reverse()
    print("".join(ls))
    

