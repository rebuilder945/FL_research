list = eval(input())
a = list.count(0)
i = 0
while i <= a:
    if 0 in list:
        list.remove(0)
        i += 1
liuyi = 0
if liuyi <= a:
    list.append(0)
    liuyi += 1
print(list)

