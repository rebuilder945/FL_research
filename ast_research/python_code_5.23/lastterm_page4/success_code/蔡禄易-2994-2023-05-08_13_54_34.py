list1 = eval(input())
n,m = eval(input())
list2 = []
for i in list1:
    if list1[n] == i:
        list2 = [i]*m
        list1 = list1 + list2
print(list1)
if len(list2) == 0:
    print("error")
