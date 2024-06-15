a = input()
n,m = eval(input())
list = a.split(',')
for i in range(len(list)):
    b = int(list[i])
    del list[i]
    list.insert(i,b)
if n < 0:
    n = len(list)+n
else:
    pass
if n >= 0 and n<len(list):
    b = list[n]
    for x in range(m):
        list.append(b)
    print(list)
else:
    print("error")
