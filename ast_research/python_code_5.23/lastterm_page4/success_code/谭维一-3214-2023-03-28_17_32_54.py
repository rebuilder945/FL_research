list = eval(input())
list_0 = []
for i in range(list):
    if i == 0:
        list.pop(i)
        list_0.append(i)
ls = list+list_0
print(ls)
