ls = eval(input())
ls.sort(reverse = True)
if ls.count(0)!=len(ls):
    for x in ls:
        print(x,end="")
else:
    print("0")
