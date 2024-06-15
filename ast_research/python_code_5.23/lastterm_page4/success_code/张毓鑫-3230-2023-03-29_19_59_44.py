a=eval(input())
a.sort(reverse=True)
if max(a)==0:
    print(0)
else:
    for i in a:
        print(i,end="")

