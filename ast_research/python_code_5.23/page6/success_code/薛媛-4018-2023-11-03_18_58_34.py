def shift(lst):
    list2=list(list1)
    a=len(list2)-1
    b=list2[a]
    list3=list(b)
    list3.append(list2[:a])
    return(list3)
    
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

