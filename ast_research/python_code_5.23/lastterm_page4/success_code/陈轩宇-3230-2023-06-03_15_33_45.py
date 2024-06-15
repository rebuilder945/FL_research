a = eval(input())
a = list(a)
a.sort()
if a[-1]==0:
    print(0)
else:
    a.reverse()
    a = list(a)
    a = map(str,a)
    print("".join(a))
    
    
