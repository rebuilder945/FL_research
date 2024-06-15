ls = eval(input())
ls.sort(reverse=True)
a = list(map(str,ls))
print("".join(a))
for x in range(len(ls)):
    if ls[x]==0:
        print(0)



