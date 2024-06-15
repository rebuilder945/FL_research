a=eval(input())
a.sort(reverse=True)
for x in a:
    if max(a)==0:
        print(0)
    else:
        print(x,end="")


