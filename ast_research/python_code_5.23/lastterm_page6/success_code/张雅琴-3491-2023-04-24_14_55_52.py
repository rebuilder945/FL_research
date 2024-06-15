def shift(lst):
    lst=input().split(",")
    lst1=list(lst)
    a=[]
    num=len(lst1)-1
    b=lst1[num]
    a.append(b)
    del lst1[num]
    c=a+lst1
    return(c)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

