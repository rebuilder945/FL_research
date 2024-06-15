ls=eval(input())
ls.sort(reverse=True)
s=""
for i in range(len(ls)):
    if ls[0] in [0]:
        print(0)
        break
    else:
        s=s+str(ls[i])
        print(s)
