def shift(lst):
    for i in range(len(lst)):
        a=[]
        while i>0:
            lst[i]=lst[i-1]
        else:
            lst[i]=lst[-1]
        a.append()
        return(a)
        

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

