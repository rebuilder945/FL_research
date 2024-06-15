def shift(lst):
        a=len(lst)
        for i in range(a-1):
           lst.append(lst[i])
         for i in range(a-1):
           lst.remove(lst[i])
        return(lst)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

