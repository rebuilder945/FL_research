def shift(lst):
for i in range(1):
        a=list(lst)
        a.pop()
        a.insert(0,a.pop())

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

