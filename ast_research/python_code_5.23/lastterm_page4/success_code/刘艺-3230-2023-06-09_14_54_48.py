ls1 = eval(input())
ls1.sort(reverse = True)
if ls1[0] == 0:
    print("0")
else:
    for x in ls1:
        print(x,end="")
