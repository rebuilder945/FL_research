a = list(eval(input()))
a.sort(reverse = True)
if a[0] == 0:
    print("0")
else:
    for x in a:
        print(x,end="")
