def shift(lst):
    
    Lst1=lst
    Lst1.reverse()
    A=Lst1.pop(0)
    Lst1.append(A)
    Lst1.reverse()
    list1=Lst1
    
    return list1
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

