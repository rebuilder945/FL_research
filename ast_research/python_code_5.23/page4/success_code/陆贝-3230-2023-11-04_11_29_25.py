a=eval(input())
a.sort()
a.reverse()
t=""
for i in a:
    x=str(i)
    t=t+x
if t[0]=="0":
    print(0)
else:
    print(t)
