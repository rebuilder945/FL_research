l = eval(input())
l.sort()
if(l[-1] == 0):
    print(0)
else:
    l = list(map(str,l))
    l.reverse()
    print("".join(l))
