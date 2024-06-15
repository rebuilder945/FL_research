s = input()
m = eval(s)
m.sort(reverse = True)
if m[0] == 0:
    del m[0]
else:
    for x in m:
        print(x,end="")
