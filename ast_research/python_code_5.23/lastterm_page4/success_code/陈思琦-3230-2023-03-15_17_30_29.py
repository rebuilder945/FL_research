a=eval(input())
a.sort()
a.reverse()
if int(a[0])==0:
    print("0")
else:
     print("".join(str(i) for i in a))
