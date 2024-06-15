ls1 = input().split(",")
ls2 = eval(input())
ls = []
for x in range(0,len(ls1)):
    y = [ls1[x],ls2[x]]
    ls.append(y)
print(ls)

