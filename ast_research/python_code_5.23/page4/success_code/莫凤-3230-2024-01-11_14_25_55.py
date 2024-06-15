a=eval(input())
a.sort(reverse=True)
s=""
if max(a)==0:
    print("0")
else:
    for x in a:
        s+=str(x)
    print(s)
