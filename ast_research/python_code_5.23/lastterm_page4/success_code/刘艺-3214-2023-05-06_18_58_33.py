list = eval(input())
a = list.count(0)
for x in list:
    if x==0:
        list.remove(x)
liuyi = 1
while liuyi <= a:
    list.append(0)
    liuyi += 1
print(list)

