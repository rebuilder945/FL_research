def shift(lst):
def  shift(lst): 
    ls2=lst.copy()
    for i in range(len(lst)):
        ls2[i]=lst[i-1]
    lst[:] = ls2
    return None

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

