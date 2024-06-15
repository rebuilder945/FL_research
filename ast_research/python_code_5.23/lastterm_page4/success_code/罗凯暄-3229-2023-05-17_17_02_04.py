list = eval(input())
n = []
for num in list:
    if list.count(num) == 1:
        n.append(num)
if len(n) == 0:
    print(False)
else:
    for i in n:
        print(i,end=',')
