def shift(lst):
    temp =1st[-1]
    for i in range(len(lst)-1,0,-1): 
        Ist[i]=lst[i-1] 
    Ist[0]=temp

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

