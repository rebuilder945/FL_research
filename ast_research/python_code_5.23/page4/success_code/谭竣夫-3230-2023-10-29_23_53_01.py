a=eval(input())
a.sort(reverse=True)   
if max(a)==0:
    print()
else:
    for x in a:
        print(x,end="")


