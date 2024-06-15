list1=eval(input())
a,b=eval(input())
if not "a" in list1 or not "b" in list1:
    print("error")
elif "a" in list1 and "b" in list1:
    list2=list1.remove("a")
    list3=list2.remove("b")
    print(list3)


