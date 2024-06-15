def shift(lst):
    pop1=lst.pop(-1)
    lst.insert(pop1,0)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

