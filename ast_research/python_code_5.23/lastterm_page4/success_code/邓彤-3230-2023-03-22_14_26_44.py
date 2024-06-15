a=eval(input())
a.sort(reverse=True)
for x in a:
    if int(x)>0:
        print(int(x),end=(""))
    else:
        print("0")
