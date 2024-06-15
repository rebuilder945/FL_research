def shift(lst):
    new=[]
    new.append(lst[len(lst)-1])
    for x in lst[0:len(lst)-1]:
        new.append(x)
    list1=new

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

