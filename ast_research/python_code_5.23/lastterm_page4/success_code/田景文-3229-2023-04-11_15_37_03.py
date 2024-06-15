sums = eval(input())
x = []
for i in sums:
    if sums.count(i) == 1:
        x.append(i)
x.sort(reverse=False)
if x == []:
    print(False)
else:
    print(*x,sep=",")
