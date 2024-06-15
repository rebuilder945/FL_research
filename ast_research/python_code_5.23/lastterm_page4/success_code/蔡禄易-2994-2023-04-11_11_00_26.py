list1 = list(eval(input()))
n,m = eval(input())
list2 = []
list3 = []
for i in list1:
    if list1.index(i) == n:
        list2 = [i]
        list3 = list2*m
list4 = list1+list3
if len(list2) == 0:
    print(False)
else:
    print(list4)
