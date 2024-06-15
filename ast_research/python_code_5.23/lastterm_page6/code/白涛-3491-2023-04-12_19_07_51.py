def shift(lst):
a=list(lst[-1])
a.append(lst[1;0])
return(a)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

