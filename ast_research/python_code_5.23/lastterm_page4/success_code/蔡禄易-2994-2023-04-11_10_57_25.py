list1 = list(eval(input()))
n,m = eval(input())
list2 = []
for i in list1:
    if list1.index(i) == n:
        list2 = [i*m]
list3 = list1+list2
if len(list2) == 0:
    print(False)
else:
    print(list3)
