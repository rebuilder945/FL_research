ls = list(eval(input()))
if ls==0:
    print(0)
else:
    ls.sort(reverse=True)
    for i in range(len(ls)):
        print(ls[i],end="")

