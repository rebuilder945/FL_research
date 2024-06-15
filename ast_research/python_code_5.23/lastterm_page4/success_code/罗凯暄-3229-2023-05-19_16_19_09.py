list = eval(input())
n = []
for num in list:
    if list.count(num) == 1:
        n.append(num)
        n.sort()
if len(n) == 0:
    print(False)
else:
        print(*n,sep=',')

