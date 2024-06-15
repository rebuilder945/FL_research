m=eval(input())
m.sort()
m.reverse()
if max(m) == 0:
    print("0")
else:
    for i in m:
        print (i,end="")
