def shift(lst):
 a=list(lst)
    a.pop(len(a)-1)
    b=a.pop(len(a)-1)
    lst=a+b

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

