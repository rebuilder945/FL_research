def shift(lst):
a=list1.pop(-1)
list1.insert(a,0)
return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

