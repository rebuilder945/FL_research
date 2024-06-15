def shift(lst):
for i in range(1):
    ilist=list(lst)
    ilist.pop()
    ilist.insert(0,ilist.pop())
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

