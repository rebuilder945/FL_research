list1 = eval(input())
a,b = eval(input())
if a in list1 and b in list1:
    for i in range(list1.index(b)-list1.index(a)-1):
        list1.pop(list1.index(a)+1)
    print(list1)
else:
    print("error")
