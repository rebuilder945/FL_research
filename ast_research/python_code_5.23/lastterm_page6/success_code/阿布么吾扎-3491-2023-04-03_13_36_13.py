def shift(lst):
    for x in lst:
        A.insert(0,A.pop())
    return A 
   

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

