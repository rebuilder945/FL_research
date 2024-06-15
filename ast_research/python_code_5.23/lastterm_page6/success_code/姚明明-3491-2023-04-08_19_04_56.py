def shift(lst):
    a=eval(input())
    lst=list(a)
    b=len(lst)
    c=lst[b-1]
    lst.remove(c)
    list1=lst.insert(0,'c')

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

