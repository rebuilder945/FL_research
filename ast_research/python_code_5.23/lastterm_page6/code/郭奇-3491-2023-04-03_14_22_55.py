def shift(lst):
def shift(lst1):
    n = len(lst)
    last = lst1[-1]
    for i in range(n-1,0,-1):
        lst1[i] = lst1[i-1]
    lst1[0] = last

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

