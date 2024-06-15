list1 = eval(input())
a,b = eval(input())
list2 = []
if 0<=a<=b<len(list1):
    for i in range(len(list1)):
        if a==b:
            list2.append(list1[i])
        else:
            if i < a or i >= b:
                list2.append(list1[i])
    print(list2)
else:
    print("error")
