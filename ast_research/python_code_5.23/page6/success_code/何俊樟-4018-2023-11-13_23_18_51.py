def shift(lst):
    for x in range(1,len(lst)):
        a=lst[-x]
        b=lst[-x-1]
        lst[-x]=b
        lst[-x-1]=a
        

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

