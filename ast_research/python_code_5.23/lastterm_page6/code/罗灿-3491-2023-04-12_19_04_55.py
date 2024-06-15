def shift(lst):
tmp=list[-1]
list.insert(0,tmp)
list.pop(-1)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

