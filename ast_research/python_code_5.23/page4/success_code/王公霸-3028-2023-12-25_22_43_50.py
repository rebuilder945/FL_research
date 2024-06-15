a,b,c = eval(input())
list = [1]
list[0] = a
for x in range(0,b-1):
    a+=c
    list.append(a)
print(list)
