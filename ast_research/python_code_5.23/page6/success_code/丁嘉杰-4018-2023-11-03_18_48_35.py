def shift(lst):
    a=len(list1)
    b=list1[a-1]
    ls1=[0 for i in range(0,a)]
    j=1
    ls1[0]=b
    for i in list1[0:-1]:
        ls1[j]=i
        j+=1
    return ls1


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

