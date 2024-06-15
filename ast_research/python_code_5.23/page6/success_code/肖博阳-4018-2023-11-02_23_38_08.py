def shift(lst):
    lst.pop(-1)
    lst.insert(0,"a")
    
    
    
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

