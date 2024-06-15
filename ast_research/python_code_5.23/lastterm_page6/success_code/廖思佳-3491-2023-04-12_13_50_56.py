def shift(lst):
    n=len(lst)
    for i in range(n):
        if i !=n-1 :
            lst[i]=lst[i+1]
        else:
            lst[i]=lst[0]

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

