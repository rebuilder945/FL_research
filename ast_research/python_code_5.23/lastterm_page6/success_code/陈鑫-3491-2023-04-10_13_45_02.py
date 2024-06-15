def shift(lst):
    b=[]
    b.append(lst[-1])
    b+=lst
    b.pop(-1)
    b=list(map(str,b))
    return b


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

