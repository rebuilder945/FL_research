def shift(lst):
    a=len(lst)-1
    bst=[lst[a]]
    
    del lst[a]
    cst=bst+lst
    return cst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

