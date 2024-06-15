def remove(list1):
    new=[]
    for i in list1:
        if i not in new:
            new.append(i)
    print(new)
a=eval(input())
remove(a)
