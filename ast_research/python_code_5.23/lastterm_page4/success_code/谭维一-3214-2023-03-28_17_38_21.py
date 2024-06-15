list = eval(input())
list_0 = []
for i in range(len(list)-1,-1,-1):
    if list[i]== 0:
        a = list.pop(i)
        list_0.append(a)
ls = list+list_0
print(ls)
