list1=eval(input())
list1.sort(reverse=True)
if list1.count(0)!=len(list1):
    for x in list1:
        print(x,end=(""))
else:
    pass
    print("0")
