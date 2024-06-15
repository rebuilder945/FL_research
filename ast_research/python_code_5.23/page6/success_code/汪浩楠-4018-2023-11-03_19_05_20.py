def shift(lst):
    a=lst[len(lst)-1]
    for i in reversed( range(len(lst)-1)):
        lst[i+1]=lst[i]
        lst[0]=a
    return(lst)
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

