def shift(lst):
        n=lst.pop(0)
        lst= lst.insert(0,n)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

