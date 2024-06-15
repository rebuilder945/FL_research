def shift(lst):
    n1ew=[]
    n1ew.append(lst[len(lst)-1])
    for x in lst[0:len(lst)-1]:
        n1ew.append(x)
    lst=n1ew

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

