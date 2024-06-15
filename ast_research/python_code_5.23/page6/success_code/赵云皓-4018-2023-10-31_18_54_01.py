def shift(lst):
    a=[]
    for x in lst:
        if lst.index(x)+2>len(lst):
            b=lst.index+1
            a.insert(b,x)
        else:
            a.insert(0,x)
    return a    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

